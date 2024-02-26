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
        self._book_title = title
        self._author_name = author
        self._which_genre = genre
        self.start_date = None
        self.end_date = None
        self._read_length = None
        self.__info = None
        # accessing the instance_count variable of the Book class and adding 1 to its value
        Book.instance_count += 1

    # Encapsulation - __info variable cannot be directly assigned new values outside of this class
    # Protects the __info attribute from changing
    def get_info(self):
        __info = {'Title': self._book_title, 'Author': self._author_name, 'Genre': self._which_genre}
        return __info

    def set_start_date(self, day=None, month=None, year=None):
        if None in [day, month, year]:
            current_date = datetime.now()
            self.start_date = str(current_date.date()).split('-')
            self.start_date = [int(self.start_date[2]), int(self.start_date[1]), int(self.start_date[0])]
        else:
            self.start_date = [day, month, year]

    def get_start_date(self):

        return self.start_date

    def set_end_date(self, day=None, month=None, year=None):
        if None in [day, month, year]:
            current_date = datetime.now()
            self.end_date = str(current_date.date()).split('-')
            self.end_date = [int(self.end_date[2]), int(self.end_date[1]), int(self.end_date[0])]
        else:
            self.end_date = [day, month, year]

    def get_end_date(self):

        return self.end_date

    # Polymorphism - Operator overloading
    def __str__(self):
        return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nStart: '
                f'{self.start_date}\nEnd: {self.end_date}')

    # del method is called when an object is about to be destroyed
    def __del__(self):
        # accessing the instance_count variable of the Book class and subtracting 1 from its value
        Book.instance_count -= 1


# Inheritance - inherits Book class' attributes & methods
class Chapter(Book):
    # will directly pass arguments later to become attributes of the super class and subclass
    def __init__(self, title, author, genre, pages):
        super().__init__(title, author, genre)
        self._pages_count = pages
        self.pages_finished = 0

    # Polymorphism - method overriding
    def get_info(self):
        __info = {'Title': self._book_title, 'Author': self._author_name, 'Genre': self._which_genre,
                  'Pages': self._pages_count}
        return __info

    def __str__(self):
        return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nPages: '
                f'{self._pages_count}\nStart: {self.start_date}\nEnd: {self.end_date}')

    def add_pages(self, pages):

        if self.pages_finished > self._pages_count:
            print('Maximum book pages reached.')
        else:
            self.pages_finished += pages

    def remove_pages(self, pages):

        if self.pages_finished <= 0:
            self.pages_finished = 0
            print('Page count at 0')
        else:
            self.pages_finished -= pages

    def get_pages_info(self):
        _percentage = round((self.pages_finished/self._pages_count) * 100)
        print(f'{self._book_title}: {_percentage}% finished\nPages finished: {self.pages_finished}/{self._pages_count}')


# Polymorphism - Duck typing - using a method interchangeably with another object
def get_all_info(object_variable):
    info = object_variable.get_info()
    print(info)
