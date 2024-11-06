# library management system
# parent class/super class
class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
    def display(self):
        return f"Title {self.title} Author {self.author}"
    # child class
class Librarybook(Book):
    def __init__(self,title, author, isbn, copies_available):
        super().__init__(title,author)
        self.isbn=isbn
        self.copies_available=copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available-=1
            return f"{self.title} borrowed. The number of copies left are {self.copies_available}"
        else:
            return f"The number of copies available are {self.copies_available}"
    def return_book(self):
        self.copies_available+=1
        return f"{self.title} returned. Available copies are{self.copies_available}"

# usage example
book1=Librarybook("The Blossoms of The Savannah", "Henry Ole Kulet",345, 100)
print(book1.display())
print(book1.borrow_book())
print(book1.return_book())
