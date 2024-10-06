# library_management.py

class Book:
    """Represents a book with a title, author, and checkout status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out if it's not already checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned, making it available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    """Represents a library that manages a collection of books."""
    
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Add a new book to the library's collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}' successfully.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")
    
    def return_book(self, title):
        """Return a book by title, making it available again."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}' successfully.")
                else:
                    print(f"'{title}' is not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")
    
    def list_available_books(self):
        """List all books that are currently available in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books at the moment.")

