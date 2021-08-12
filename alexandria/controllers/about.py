from flask import render_template

from alexandria.run import app


@app.route('/sobre', methods=['GET', 'POST'])
def sobre():
    """
    Router info project

    Returns:
        template:  render template html with about project
    """
    return render_template('about.html')