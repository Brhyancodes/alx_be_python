# book_class.py
# Create a Python script named book_class.py. In this script, define a Book class
# that uses specific magic methods to enhance its functionality.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor deletes the book object
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation of the book
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official Representation (__repr__): Returns a string that would recreate the Book instance
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage to demonstrate the magic methods
if __name__ == "__main__":
    print("=== Creating Book Instances ===")
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    print("\n=== Testing __str__ method (user-friendly) ===")
    print(book1)  # Uses __str__
    print(book2)  # Uses __str__

    print("\n=== Testing __repr__ method (developer-friendly) ===")
    print(repr(book1))  # Uses __repr__
    print(repr(book2))  # Uses __repr__

    print("\n=== Both representations side by side ===")
    print(f"str():  {str(book1)}")
    print(f"repr(): {repr(book1)}")

    print("\n=== Testing that __repr__ can recreate the object ===")
    # The __repr__ output should be valid Python code
    recreated_book = eval(repr(book1))
    print(f"Original:   {book1}")
    print(f"Recreated:  {recreated_book}")

    print("\n=== Objects will be deleted when program ends ===")
    # __del__ will be called automatically
