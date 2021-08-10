from alexandria.book_api import search_book_kan

booktitle = input(str('Informe o título do livro: '))
bookauthor = input(str('Informe o nome do autor: '))

avocado = search_book_kan(booktitle, bookauthor)

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

print('\n\n')
print('*'*10)
print(avocado)
print('\n\n')
print('*'*10)
print(avocado['title'])
print('*'*10)
print(avocado['author'])
print('*'*10)
print(avocado['isbn'])
print('*'*10)
print(avocado['categories'])
print('*'*10)
print(avocado['description'])
print('*'*10)
print(avocado['img'])
print('*'*10)
print(avocado['publisher'])
print('*'*10)
print(avocado['publishedDate'])
print('*'*10)
print(avocado['pageCount'])
print('*'*10)