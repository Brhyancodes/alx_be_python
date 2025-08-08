# library_system.py
# Develop a library system with inheritance and composition


# Base Class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"


# Derived Classes - EBook and PrintBook:
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def display_info(self):
        return f"EBook: {self.title} by {self.author}, Size: {self.file_size}MB"


# Print Book class
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = (
            page_count  # number of pages (changed from 'pages' to 'page_count')
        )

    def display_info(self):
        return f"Print Book: {self.title} by {self.author}, Pages: {self.page_count}"


# Composition - Library:
# Attributes: books (a list to store instances of Book, EBook, and PrintBook).
# Methods:
# add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
# list_books(self): Prints details of each book in the library.
class Library:
    def __init__(self):
        self.books = []  # List to store book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book.display_info()}")
        else:
            raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("Library Books:")
        print("-" * 40)
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.display_info()}")


# Example usage:
if __name__ == "__main__":
    print("=== Creating Book Instances ===")
    # Create instances of all three types
    regular_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    ebook1 = EBook("Python Programming", "John Doe", 5)
    printbook1 = PrintBook("Learning Python", "Jane Smith", 300)

    print("=== Creating Library ===")
    # Create a Library instance
    library = Library()

    print("\n=== Adding Books to Library ===")
    # Add books to the library
    library.add_book(regular_book)
    library.add_book(ebook1)
    library.add_book(printbook1)

    print("\n=== Listing All Books ===")
    # List all books in the library
    library.list_books()

    print("\n=== Testing Error Handling ===")
    try:
        library.add_book("Not a book object")  # This should raise an error
    except TypeError as e:
        print(f"Error caught: {e}")

    print("\n=== Demonstrating Inheritance ===")
    print("All objects are instances of Book:")
    print(f"regular_book instanceof Book: {isinstance(regular_book, Book)}")
    print(f"ebook1 instanceof Book: {isinstance(ebook1, Book)}")
    print(f"printbook1 instanceof Book: {isinstance(printbook1, Book)}")
