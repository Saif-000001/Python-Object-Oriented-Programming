class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_book(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("BD Public Library!")

book1 = Book('A', 'x')
book2 = Book('B', 'y')
book3 = Book('C', 'z')

print(library.name)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


for book in library.list_book():
    print(book)