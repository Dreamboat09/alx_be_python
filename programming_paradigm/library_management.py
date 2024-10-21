class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
        
    def check_out(self):
        pass
    
    def return_book(self):
        pass
    
class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self):
        pass
    
    def check_out_book(self, title):
        pass
    
    def return_book(self, title):
        pass
    
    def list_available_books(self):
        pass 