# Base Class: Book
class Book:
    def __init__(self, title, author):
        """Initialize common book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a Book."""
        return f"Book: {self.title} by {self.author}"

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize attributes for an EBook, including those inherited from Book."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize attributes for a PrintBook, including those inherited from Book."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition: Library class to manage books
class Library:
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
