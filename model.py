class Book:
    def __init__(self, title, author, reg_number):
        self.title = title
        self.author = author
        self.reg_number = reg_number
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def borrow_book(self, reg_number):
        for book in self.books:
            if book.reg_number == reg_number and not book.is_borrowed:
                book.is_borrowed = True
                return book
        return None

    def return_book(self, reg_number):
        for book in self.books:
            if book.reg_number == reg_number and book.is_borrowed:
                book.is_borrowed = False
                return book
        return None
