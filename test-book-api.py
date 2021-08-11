from kan_alexandria.book_api import search_book_kan as search

booktitle = input(str('Informe o título do livro: '))
bookauthor = input(str('Informe o nome do autor: '))

book_dict = search(booktitle, bookauthor)

for k, v in book_dict.items():
    if book_dict[k] == ' ':
        book_dict[k] = 'N/A'
if book_dict['title'] == None or book_dict['title'] == 'N/A':
    book_dict['title'] = 'request.form'
if book_dict['author'] == None or book_dict['author'] == 'N/A':
    book_dict['author'] = 'request.form'

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
print(book_dict)
print('\n\n')
print('*'*10)
print(book_dict['title'])
print('*'*10)
print(book_dict['author'])
print('*'*10)
print(book_dict['isbn'])
print('*'*10)
print(book_dict['categories'])
print('*'*10)
print(book_dict['description'])
print('*'*10)
print(book_dict['img'])
print('*'*10)
print(book_dict['publisher'])
print('*'*10)
print(book_dict['publishedDate'])
print('*'*10)
print(book_dict['pageCount'])
print('*'*10)