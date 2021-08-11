import subprocess

#functions
def search_book_kan(title=None, author=None, lang_code=None, isbn=None):
    """
    Searches the book in the internet using kan module. Provide at least one
    of the arguments. Eg. title and/or author and/or isbn. 
    Consult kan documentation for more details about the arguments.

    The result is a dict with the following keys:
    - title
    - author
    - isbn
    - categories
    - description
    - img #url to the cover image
    - publisher
    - publishedDate #YYYY-MM-DD
    - pageCount
    """

    title = "'" + title + "'" #encapsulate the title in '
    author = "'" + author + "'" #encapsulate the author in '
   
   #TODO: get the language code from user input
    #lang_code='por' #sets the default language to portuguese
    
    #search
    if lang_code is None:
        result = subprocess.run(['kan', '--title', title, '--author', author, '--max', '1',], stdout=subprocess.PIPE)
    else:
        result = subprocess.run(['kan', '--title', title, '--author', author, '--max', '1', '--language', lang_code], stdout=subprocess.PIPE)
    searchbook = result.stdout.decode('utf-8')

    #testing if the book was found
    if searchbook != None:

        #string slicing
        title_position = searchbook.find('Title: ')
        author_position = searchbook.find('Author: ')
        isbn_position = searchbook.find('ISBN')
        categories_position = searchbook.find('Categories: ')
        description_position = searchbook.find('Description: ')
        img_position = searchbook.find('IMG: ')
        publisher_position = searchbook.find('Publisher: ')
        publishedDate_position = searchbook.find('Published: ')
        pageCount_position = searchbook.find('PageCount: ')
        end_position = len(searchbook)
        
        book_dict = {
            'title': searchbook[title_position+7:author_position-1],
            'author': searchbook[author_position+8:isbn_position-1],
            'isbn': searchbook[isbn_position+8:categories_position-1],
            'categories': searchbook[categories_position+12:description_position-1],
            'description': searchbook[description_position+13:img_position-1],
            'img': searchbook[img_position+5:publisher_position-1],
            'publisher': searchbook[publisher_position+11:publishedDate_position-1],
            'publishedDate': searchbook[publishedDate_position+11:pageCount_position-1],
            'pageCount': searchbook[pageCount_position+11:end_position-1]
        }

        return book_dict

    else:
        return None