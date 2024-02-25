from datetime import datetime


# Class names always start with a capital letter
class Book:
    # instance_count variable stores how many instances of the Book class exists
    instance_count = 0

    # init is a special method called a CONSTRUCTOR that initializes the object's attributes
    # initial values are passed to this init method and stored as attributes
    # values will be accessed by other methods later on
    # self refers to the current instance of the class
    # self is used to access variables and methods associated with the current instance
    def __init__(self, title, author, genre):
        # accessing the main_title attribute of the current instance of the class
        self._main_title = title
        self._author_name = author
        self._which_genre = genre
        self.start_date = None
        self.end_date = None
        self._read_length = None
        # accessing the instance_count variable of the Book class and adding 1 to its value
        Book.instance_count += 1

    # Encapsulation - __info variable cannot be directly assigned new values outside of this class
    # Protects the __info attribute from changing
    def get_info(self):
        __info = {'Title': self._main_title, 'Author': self._author_name, 'Genre': self._which_genre}
        return __info

    def set_start_date(self, year=None, month=None, day=None):
        if None in [year, month, day]:
            current_date = datetime.now()
            self.start_date = str(current_date.date()).split('-')
        else:
            self.start_date = [year, month, day]

    def get_start_date(self):

        return self.start_date

    def set_end_date(self, year=None, month=None, day=None):
        if None in [year, month, day]:
            current_date = datetime.now()
            self.end_date = str(current_date.date()).split('-')
        else:
            self.end_date = [year, month, day]

    def get_end_date(self):

        return self.start_date

    # Polymorphism - Operator overloading
    def __sub__(self, other):
        return int(self.start_date[0]) - int(other.start_date[0])

    # del method is called when an object is about to be destroyed
    def __del__(self):
        # accessing the instance_count variable of the Book class and subtracting 1 from its value
        Book.instance_count -= 1


# Inheritance - inherits Book class' attributes & methods
class Magazine(Book):
    def __init__(self, title, publisher, issue_number):
        super().__init__(title, author=None, genre=None)
        self._publisher_name = publisher
        self._issue_number = issue_number

    # Polymorphism - method overriding
    def get_info(self):
        __info = {'Title': self._main_title, 'Publisher': self._publisher_name, 'Issue No.': self._issue_number}
        return __info


# Polymorphism - Duck typing - using a method interchangeably with another object
def get_all_info(object_variable):
    info = object_variable.get_info()
    print(info)


# Add pages and average read of all accounts
class Account:

    def __init__(self):
        self.__username = None
