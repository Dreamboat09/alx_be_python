class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = True 
        
    def check_out(self):
        if self.title and self.author:
            return self._is_checked_out()
    
    def return_book(self):
        if self.title and self.author:
            return not self._is_checked_out()
    
class Library(Book):
    def __init__(self):
        self._books = []
        self._available = True
        
    def add_book(self):
        self._books = self._books.append(Book)
    
    def check_out_book(self, title):
        for BOOK in self._books:
            if BOOK.title == title and self._available:
                print(f'{title} is ckecked out')
                self._books.remove(title)
        
    
    def return_book(self, title):
        for BOOK in self._books:
            if BOOK.title == title and not self._available:
                print(f'{title} returned')
                self._books.append(title)
        
    
    def list_available_books(self):
       for BOOK in self._books and self._available:
           print(BOOK)
