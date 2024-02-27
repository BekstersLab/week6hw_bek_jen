# Importing the datetime class from the datetime module
from datetime import datetime


# Class names always start with a capital letter
# class declares a Book class
class Book:
    # instance_count variable stores how many instances of the Book class exists
    instance_count = 0

    # init is a special method called a CONSTRUCTOR that initializes the object's attributes
    # initial values are passed to constructor method and stored as attributes
    # values will be accessed by other methods later on
    # self refers to the current instance of the class
    # self is used to access variables and methods associated with the current instance
    def __init__(self, title, author, genre):

        # accessing the book_title attribute of the current instance of the class
        # Encapsulation - restricting access to certain parts of the class
        # Encapsulation provides data protection and prevents direct manipulation of certain parts of the class
        # adding an _ to an attribute name means it is 'protected'
        # _ cannot be directly assigned a value, it has to be accessed through a method or subclasses
        # dunderscore means this is 'private' and should only be accessed within this class and not subclasses
        self._book_title = title
        self._author_name = author
        self._which_genre = genre

        # Initially assigning None to these attributes so that their values can only be assigned through methods
        self._start_date = None
        self._end_date = None
        self._read_length = None

        # accessing the instance_count variable of the Book class and adding 1 to its value
        Book.instance_count += 1

    # def declares the set_start_date method with 4 parameters, 3 parameters have the default value
    def set_start_date(self, day=None, month=None, year=None):

        if None in [day, month, year]:
            # datetime is a class, now is a method
            current_date = datetime.now()
            self._start_date = str(current_date.date()).split('-')
            self._start_date = [int(self._start_date[2]), int(self._start_date[1]), int(self._start_date[0])]
        else:
            self._start_date = [day, month, year]

    def get_start_date(self):

        return self._start_date

    def set_end_date(self, day=None, month=None, year=None):
        if None in [day, month, year]:
            current_date = datetime.now()
            self._end_date = str(current_date.date()).split('-')
            self._end_date = [int(self._end_date[2]), int(self._end_date[1]), int(self._end_date[0])]
        else:
            self._end_date = [day, month, year]

    def get_end_date(self):

        return self._end_date

    # Polymorphism - Operator overloading
    # Customising the behaviour of predefined operators or special methods when they are applied to instances of a class
    def __str__(self):
        if self._end_date is None:

            return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nStart: '
                    f'{self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd: {self._end_date}')

        else:

            return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nStart: '
                    f'{self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd: {self._end_date[0]}/'
                    f'{self._end_date[1]}/{self._end_date[2]}')

    # del method is called when an object is about to be destroyed
    def __del__(self):
        # accessing the instance_count variable of the Book class and subtracting 1 from its value
        Book.instance_count -= 1


# SUB CLASS ------------------------------------------------------------------------------------------------------------
# Inheritance - inherits Book class' attributes & methods
# This is single inheritance, but there is also multiple inheritance, multi-level inheritance & hierarchical inheritance
class Chapter(Book):
    # will directly pass arguments later to become attributes of the super class and subclass
    def __init__(self, title, author, genre, pages):
        super().__init__(title, author, genre)
        self._pages_count = pages
        self.pages_finished = 0

    # Polymorphism - method overriding
    def set_end_date(self, day=None, month=None, year=None):
        self.pages_finished = self._pages_count

        if None in [day, month, year]:
            current_date = datetime.now()
            self._end_date = str(current_date.date()).split('-')
            self._end_date = [int(self._end_date[2]), int(self._end_date[1]), int(self._end_date[0])]
        else:
            self._end_date = [day, month, year]

    # def get_info(self):
    #     __info = {'Title': self._book_title, 'Author': self._author_name, 'Genre': self._which_genre,
    #               'Pages': self._pages_count}
    #     return __info

    def set_pages(self, pages):

        if self.pages_finished >= self._pages_count:
            print('Maximum book pages reached.')
            self.pages_finished = self._pages_count
        else:
            self.pages_finished = pages

    def get_pages_info(self):
        _percentage = round((self.pages_finished/self._pages_count) * 100)
        print(f'{self._book_title}: {_percentage}% Done\n{self.pages_finished}/{self._pages_count} pages finished')

    def __str__(self):

        if self._end_date is None:

            return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nPages: '
                    f'{self._pages_count}\nStart: {self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\n'
                    f'End: {self._end_date}')

        else:

            return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nPages: '
                    f'{self._pages_count}\nStart: {self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd:'
                    f' {self._end_date[0]}/{self._end_date[1]}/{self._end_date[2]}')


if __name__ == '__main__':
    # OBJECT 1 - TESTING DATES & OBJECT INSTANTIATION
    # Passing string arguments to become attributes & instantiating the midnight_book object of the Book class
    midnight_book = Book('The Midnight Library', 'Matt Haig', 'Fiction')

    # Invoking the set_start_date method of the Book class, setting a date for when the book started
    # date is stored in the _start_date attribute of the midnight_book object
    midnight_book.set_start_date(12, 5, 2023)

    # Invoking the set_end_date method of the Book class
    # When no arguments are passed, today's date is assigned to the _end_date attribute of the midnight_book object
    midnight_book.set_end_date()

    print(midnight_book, '\n')

    # OBJECT 2 - TESTING PAGES -----------------------------------------------------------------------------------------
    britney_book = Chapter('The Woman in Me', 'Britney Spears', 'Memoir', 287)

    britney_book.set_start_date(29, 9, 2023)

    print(britney_book, '\n')
    britney_book.set_pages(100)
    britney_book.get_pages_info()
    print('\n')
    britney_book.set_pages(25)
    britney_book.get_pages_info()

    # DUCK TYPING ------------------------------------------------------------------------------------------------------
    # Polymorphism - Duck typing - using a method interchangeably with another object

    # INSTANCE COUNT ---------------------------------------------------------------------------------------------------
    print(f'\nInstance Count: {britney_book.instance_count}')

    del britney_book

    print(f'Instance Count: {midnight_book.instance_count} (deleted 1 instance)')
