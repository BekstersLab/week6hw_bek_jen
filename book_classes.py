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
        # accessing the book_title attribute of the current instance of the class
        # adding an _ means it id 'protected'
        # It cannot be directly assigned a value, it has to be through a method or subclasses
        self._book_title = title
        self._author_name = author
        self._which_genre = genre
        self._start_date = None
        self._end_date = None
        self._read_length = None
        # dunderscore means this is 'private' and should only be accessed within the super class
        self.__info = None
        # accessing the instance_count variable of the Book class and adding 1 to its value
        Book.instance_count += 1

    # Encapsulation - __info variable cannot be directly assigned new values outside of this class
    # Protects the __info attribute from changing, but values can be accessed.
    def get_info(self):
        __info = {'Title': self._book_title, 'Author': self._author_name, 'Genre': self._which_genre}
        return __info

    def set_start_date(self, day=None, month=None, year=None):
        if None in [day, month, year]:
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
        return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nStart: '
                f'{self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd: {self._end_date[0]}/'
                f'{self._end_date[1]}/{self._end_date[2]}')

    # del method is called when an object is about to be destroyed
    def __del__(self):
        # accessing the instance_count variable of the Book class and subtracting 1 from its value
        Book.instance_count -= 1


# Inheritance - inherits Book class' attributes & methods
# This is single inheritance, but there is also multiple inheritance, multi-level inheritance & hierarchical inheritance
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
                f'{self._pages_count}\nStart: {self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd:'
                f' {self._end_date[0]}/{self._end_date[1]}/{self._end_date[2]}')

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
        print(f'{self._book_title}: {_percentage}% Done\n{self.pages_finished}/{self._pages_count} pages finished')


# Polymorphism - Duck typing - using a method interchangeably with another object
def get_all_info(object_variable):
    info = object_variable.get_info()
    print(info)


if __name__ == '__main__':
    # Object 1
    midnight_book = Book('The Midnight Library', 'Matt Haig', 'Fiction')

    midnight_book.set_start_date(12, 5, 2023)

    midnight_book.set_end_date(22, 8, 2023)

    print(midnight_book, '\n')

    # Object 2 ---------------------------------------------------------------------------------------------
    britney_book = Chapter('The Woman in Me', 'Britney Spears', 'Memoir', 287)

    britney_book.set_start_date(29, 9, 2023)

    britney_book.set_end_date()

    print(britney_book, '\n')

    britney_book.add_pages(150)

    britney_book.get_pages_info()

    print('\n')
    get_all_info(britney_book)
    get_all_info(midnight_book)
