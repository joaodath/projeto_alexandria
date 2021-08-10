# from flask import make_response
# from functools import wraps, update_wrapper
# from datetime import datetime

# def nocache(view):
#     @wraps(view)
#     def no_cache(*args, **kwargs):
#         response = make_response(view(*args, **kwargs))
#         response.headers['Last-Modified'] = datetime.now()
#         response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
#         response.headers['Pragma'] = 'no-cache'
#         response.headers['Expires'] = '-1'
#         return response
        
#     return update_wrapper(no_cache, view)

import datetime
import time
from functools import wraps
from wsgiref.handlers import format_date_time
from flask import make_response

# from flask import make_response
# r = make_response(render_template('index.html'))
# r.headers.set('Content-Security-Policy', "default-src 'self'")
# return r

def cache(expires=None, round_to_minute=False):
    """
    Add Flask cache response headers based on expires in seconds.
    
    If expires is None, caching will be disabled.
    Otherwise, caching headers are set to expire in now + expires seconds
    If round_to_minute is True, then it will always expire at the start of a minute (seconds = 0)
    
    Example usage:
    
    @app.route('/map')
    @cache(expires=60)
    def index():
      return render_template('index.html')
    
    """
    def cache_decorator(view):
        @wraps(view)
        def cache_func(*args, **kwargs):
            now = datetime.datetime.now()
 
            response = make_response(view(*args, **kwargs))
            response.headers.set('Last-Modified', format_date_time(time.mktime(now.timetuple())))
            
            if expires is None:
                # r.headers.set('Content-Security-Policy', "default-src 'self'") - New Way
                #response.headers.set['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0' - Old Way
                response.headers.set('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0')
                response.headers.set('Expires', '-1')
                response.headers.set('Teste-Joao-no-cache', 'deu-certo!')
            else:
                expires_time = now + datetime.timedelta(seconds=expires)

                if round_to_minute:
                    expires_time = expires_time.replace(second=0, microsecond=0)

                response.headers.set('Cache-Control', 'public')
                response.headers.set('Expires', format_date_time(time.mktime(expires_time.timetuple())))
                response.headers.set('Teste-Joao-cache', 'deu-certo!')
 
            return response
        return cache_func
    return cache_decorator