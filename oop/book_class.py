#creation of Book class
class Book:
    #creation of the constructor
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author
        self.year = year
    
    #creation of the destructor
    def __del__(self):
        print(f"Deleting {self.title}")
    
    #creation of the String Representation 
    def __str__(self):
        return "{title} by {author}, published in {year}"

    #creation of the Official Representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"