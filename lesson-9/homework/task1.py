class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def __str__(self):
        return f"Book(title: {self.title}, author: {self.author}, borrowed: {self.is_borrowed})"
class Member:
    max_books = 3
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.max_books:
            raise MemberLimitExceededException(f"{self.name} has exceeded the limit of {self.max_books} books")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"book {book.title} has already been borrowed")
        self.borrowed_books.append(book)
        book.is_borrowed = True
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            raise BookNotFoundException(f" {self.name} hasn't borrowed the book {book.title}")
    def __str__(self):
        return f"{self.name} has borrowed {len(self.borrowed_books)} number of books"
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_member(self, member):
        self.members.append(member)
        print(f"{member} added successfully!")
    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added successfully!")
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book {title} not found")
    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
            
        raise Exception(f"Member {name} not found")
    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)
        print(f"{member_name} successfully borrowed '{book_title}'")
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)
        print(f"{member_name} successfully returned '{book_title}'")
def test_library_system():
    library = Library()
    
    book1 = Book("1984", "George Orwell")
    library.add_book(book1)
    
    member1 = Member("Alice")
    library.add_member(member1)
    
    library.borrow_book("Alice", "1984")
    library.return_book("Alice", "1984")

test_library_system()