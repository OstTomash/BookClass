class Book:
    """A simple class to represent a book.

     This class allows users to create a book with given title and author,
     and compare books by attributes

     Attributes:
         - title (str): The title of the book
         - author (str): The author of the book

     Methods:
         - __init__(self): Initializes a new book with the given attributes
         - __eq__(self, other): Returns true if title and author are the same
         - __ne__(self, other): Returns true if title and author are not the same

     Example usage:
        >>> book1 = Book('Harry', 'Joan')
        >>> book2 = Book('Potter', 'Rouling')
        >>> book3 = Book('Harry', 'Joan')
        >>> print(book1 == book2)
        False
        >>> print(book1 != book2)
        True
        >>> print(book1 != book3)
        False
        >>> print(book1 == book3)
        True
    """
    def __init__(self, title, author):
        """Initializes a new book with the given title and author"""
        self.title = title
        self.author = author

    def __eq__(self, other):
        """Returns true if title and author are the same

        Raise:
            TypeError: 'Object must be instances of class Book'
        """
        if not isinstance(other, Book):
            raise TypeError('Object must be instances of class Book')

        return self.title == other.title and self.author == other.author

    def __ne__(self, other):
        """Returns true if title and author are not the same

        Raise:
            TypeError: 'Object must be instances of class Book'
        """
        if not isinstance(other, Book):
            raise TypeError('Object must be instances of class Book')

        return self.title != other.title and self.author != other.author


book1 = Book('Harry', 'Joan')
book2 = Book('Potter', 'Rouling')

print(book1 == book2)
print(book1 != book2)
