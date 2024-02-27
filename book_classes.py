# Simple Book Tracker for Kids

# abc module helps you define an abstract base class (ABC)
# An ABC is a class that is meant to be subclassed, but not instantiated directly
# ABC defines a common interface that subclasses must follow by implementing certain methods
from abc import ABC, abstractmethod

# Importing the datetime class from the datetime module to create an instance in two methods
from datetime import datetime


# Class names always start with a capital letter
# class statement defines a new class, BookTracker
# ABC indicates this is an abstract class, defining a common interface that subclasses must implement
class BookTracker(ABC):

    # @abstractmethod decorator marks a method as abstract within an abstract base class
    # @abstractmethod indicates subclasses must provide their own implementations of this method
    # track_progress method should return current info about book reading progress, how each subclass uniquely tracks it
    @abstractmethod
    def track_progress(self):
        # pass is a placeholder indicating that this method has no implementation in the ABC
        pass

    # award_badge method returns a string, awarding a badge, after a specific amount of reading progress is made.
    @abstractmethod
    def award_badge(self):
        # pass is a placeholder indicating that this method has no implementation in the ABC
        pass


# class statement defines a book class
class DatesLevel(BookTracker):
    # instance_count variable stores how many instances of the Book class exists
    instance_count = 0

    # init is a special method called a CONSTRUCTOR that initializes the object's attributes
    # initial values are passed to constructor method and stored as attributes
    # values will be accessed by other methods later on
    # self refers to the current instance of the class
    # self is used to access variables and methods associated with the current instance
    def __init__(self, title, author, genre):

        self._book_title = title
        self._author_name = author
        self._which_genre = genre
        self._read_period = None
        
        # accessing the book_title attribute of the current instance of the class
        # Encapsulation - restricting access to certain parts of the class
        # Encapsulation provides data protection and prevents direct manipulation of certain parts of the class
        # adding an _ to an attribute name means it is 'protected'
        # _ cannot be directly assigned a value, it has to be accessed through a method or subclasses
        # dunderscore means this is 'private' and should only be accessed within this class and not subclasses

        # Initially assigning None to these attributes so that their values can only be assigned through methods
        self._start_date = None
        self._end_date = None
        # accessing the instance_count variable of the Book class and adding 1 to its value
        DatesLevel.instance_count += 1

    # def declares the set_start_date method with 4 parameters, 3 parameters have the default value
    def set_start_date(self, day=None, month=None, year=None):

        if None in [day, month, year]:
            # datetime is a class, now is a method
            current_date = datetime.now()
            self._start_date = current_date.date()
            self._start_date = str(current_date.date()).split('-')
            self._start_date = [self._start_date[2], self._start_date[1], self._start_date[0]]
        else:
            self._start_date = [str(day), str(month), str(year)]

    def get_start_date(self):

        return self._start_date

    def set_end_date(self, day=None, month=None, year=None):
        if None in [day, month, year]:
            current_date = datetime.now()
            self._end_date = str(current_date.date()).split('-')
            self._end_date = [self._end_date[2], self._end_date[1], self._end_date[0]]
        else:
            self._end_date = [str(day), str(month), str(year)]

    def get_end_date(self):

        return self._end_date

    def track_progress(self):

        if self._end_date is None:
            return 'Book is not yet finished'

        else:
            # Instantiated 2 objects of the datetime class
            __start_date = datetime(int(self._start_date[2]), int(self._start_date[1]), int(self._start_date[0]))
            __end_date = datetime(int(self._end_date[2]), int(self._end_date[1]), int(self._end_date[0]))
            self._read_period = (__end_date - __start_date).days

            return f'Finished reading in {self._read_period} days'

    def award_badge(self):
        if self._end_date is not None:
            return f'You finished {self._book_title} - Here\'s a BOOK Badge!'

    # Polymorphism - Operator overloading
    # Customising the behaviour of predefined operators or special methods when they are applied to instances of a class
    def __str__(self):

        __end = None

        if self._end_date is not None:

            __end = '/'.join(self._end_date)

        return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nStart: '
                f'{self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd: {__end}\n'
                f'{self.track_progress()}')

    # del method is called when an object is about to be destroyed
    def __del__(self):
        # accessing the instance_count variable of the Book class and subtracting 1 from its value
        DatesLevel.instance_count -= 1


# SUB CLASS ------------------------------------------------------------------------------------------------------------
# Inheritance - inherits Book class' attributes & methods
# This is single inheritance, but there is also multiple inheritance, multi-level inheritance & hierarchical inheritance
class PagesLevel(DatesLevel):
    # will directly pass arguments later to become attributes of the super class and subclass
    def __init__(self, title, author, genre, pages):
        super().__init__(title, author, genre)
        self._pages_count = pages
        self.pages_finished = 0
        self.__percentage = 0

    # Polymorphism - method overriding
    def set_end_date(self, day=None, month=None, year=None):
        self.pages_finished = self._pages_count

        if None in [day, month, year]:
            current_date = datetime.now()
            self._end_date = str(current_date.date()).split('-')
            self._end_date = [self._end_date[2], self._end_date[1], self._end_date[0]]
        else:
            self._end_date = [day, month, year]

    def set_pages(self, pages):

        if self.pages_finished >= self._pages_count:
            print('Maximum book pages reached.')
            self.pages_finished = self._pages_count
        else:
            self.pages_finished = pages

    def track_progress(self):
        self.__percentage = round((self.pages_finished / self._pages_count) * 100)
        return f'{self._book_title}: {self.__percentage}% Done\n{self.pages_finished}/{self._pages_count} pages finished'

    def award_badge(self):
        if self._end_date is not None:
            return f'You finished {self._book_title} - Here\'s a BOOK Badge!'

        elif self.__percentage in range(25,51):
            return f'You finished 1/4 of {self._book_title} so far! Here\'s a BRONZE Star!'

        elif self.__percentage in range(50,76):
            return f'You finished 1/2 of {self._book_title} so far! Here\'s a SILVER Star!'

        else:

            return f'You finished 3/4 of {self._book_title}. So close! Here\'s a GOLD Star!'


    def __str__(self):

        __end = None

        if self._end_date is not None:
            __end = '/'.join(self._end_date)

        return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nPages: '
                f'{self._pages_count}\nStart: {self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd:'
                f' {__end}\n{self.track_progress()}')


if __name__ == '__main__':
    # OBJECT 1 - TESTING DATES & OBJECT INSTANTIATION ------------------------------------------------------------------
    # Passing string arguments to become attributes & instantiating the midnight_book object of the Book class
    midnight_book = DatesLevel('The Midnight Library', 'Matt Haig', 'Fiction')

    # Invoking the set_start_date method of the Book class, setting a date for when the book started
    # date is stored in the _start_date attribute of the midnight_book object
    midnight_book.set_start_date(12, 5, 2023)

    # Invoking the set_end_date method of the Book class
    # When no arguments are passed, today's date is assigned to the _end_date attribute of the midnight_book object
    midnight_book.set_end_date()

    print(midnight_book, '\n')

    # OBJECT 2 - TESTING PAGES -----------------------------------------------------------------------------------------
    britney_book = PagesLevel('The Woman in Me', 'Britney Spears', 'Memoir', 287)

    britney_book.set_start_date(29, 9, 2023)

    britney_book.set_pages(100)
    print(britney_book, '\n')

    # BOOK TRACKING & AWARDS
    print(midnight_book.track_progress(), '\n')
    print(britney_book.track_progress(), '\n')

    print(midnight_book.award_badge())
    print(britney_book.award_badge())

    # DUCK TYPING ------------------------------------------------------------------------------------------------------
    # Polymorphism - Duck typing - using a method interchangeably with another object

    # INSTANCE COUNT ---------------------------------------------------------------------------------------------------
    print(f'\nInstance Count: {britney_book.instance_count}')

    del britney_book

    print(f'Instance Count: {midnight_book.instance_count} (deleted 1 instance)')
