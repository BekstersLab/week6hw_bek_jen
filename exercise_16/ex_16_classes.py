# classes are blueprints or recipes that we can later use to create objects from
# a class describes what properties and functionality individual objects will contain
# use a class to create individual instances (objects) made from that blueprint (class) - instance of class
# class name always starts with a capital letter

# inheritance - shared attributes all have
# define a class (Person) that has the base; firstname, middlename, lastname, email
# Employee and Customer will inherit from user but have their own attributes

class Person:
    # __init__ is a special method called the CONSTRUCTOR which starts/ends in dunderscore - it is special
    # anything inside it will be called when we create a new Person
    # Person is a pattern, __init__ is a method called when we instantiate a new Person
    def __init__(self, firstname, middlename, lastname, email):
        self.first_name = firstname
        self.middle_name = middlename
        self.__last_name = lastname
        self.email = email

    # instance method - it can know about each different instance of Person and access different properties on self
    def get_firstname(self):
        return self.first_name

    def get_middlename(self):
        return self.middle_name

    def get_lastname(self):
        return self.__last_name

    def get_email(self):
        return self.email


class Employee(Person):
    def __init__(self, firstname, middlename, lastname, email, id_number, department):
        # use super() to refer to the base or parent class
        # in this case we use super() to access the __init__ method from the Person class
        # calls the constructor function (__init__) from the parent class
        # Employee now uses parent class (Person) but adds its own stuff on
        super().__init__(firstname, middlename, lastname, email)  # Call the parent class constructor
        self.id_number = id_number  # Unique to Employee
        self.department = department  # Unique to Employee

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department











