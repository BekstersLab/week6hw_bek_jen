# ENCAPSULATION
# encapsulation helps to achieve a design where the internal representation of an object is hidden from the outside,
# only exposing what is necessary. This leads to better-structured, more secure, and easily maintainable code
# examples here are _balance (protected - one underscore) and __last_name (private - two underscores)
# access to these attributes is controlled through methods, hiding the internal representation from the external use

class Account:
    numCreated = 0

    def __init__(self, nickname, account_type, initial_amount, firstname, middlename, lastname, age):
        self._balance = initial_amount
        self.nick_name = nickname
        self.first_name = firstname
        self.middle_name = middlename
        self.__last_name = lastname
        self.age = age
        self.account = account_type
        Account.numCreated += 1

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount >= 0:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    def get_firstname(self):
        return self.first_name

    def get_middlename(self):
        return self.middle_name

    def get_lastname(self):
        return self.__last_name

    def get_nickname(self):
        return self.nick_name

    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname

    def get_age(self):
        return self.age

    def get_account_type(self):
        return self.account

    # MAGIC METHOD
    # __str__ is a special method that returns a string representation of an object. It is called by the print() function
    def __str__(self):
        return (f"Account"
                f"\nNickname: {self.get_nickname()}"
                f"\nAccount Type: {self.get_account_type()}"
                f"\nFirstname: {self.get_firstname()}"
                f"\nMiddlename: {self.get_middlename()}"
                f"\nLastname: {self.get_lastname()}"
                f"\nAge: {self.get_age()}"
                f"\nBalance: ${self.get_balance()}"
                f"\n********************")