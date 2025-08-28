class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    return_book(self)
    def check_out(self, title):
        if title == self.title:
            self._is_checked_out = False

    def return_book(self, title):
        if title == self.title:
            self._is_checked_out = True



class Library:
    def __init__(self):
        self._books = []

    def add_book(self, Book):
        self._books.append(Book)

    def check_out_book(self, title):
        for book in self._books:
            if title == book.title:
                return self._is_checked_out

    def return_book(self, title):
        for book in self._books:
            return self._is_checked_out
        
    def list_available_books(self):
        for book in self._books:
            return book 