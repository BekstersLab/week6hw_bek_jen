class Person:
    def __init__(self, firstname, middlename, lastname, email):
        self.first_name = firstname
        self.middle_name = middlename
        self.__last_name = lastname
        self.email = email


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
        super().__init__(firstname, middlename, lastname, email)  # Call the parent class constructor
        self.id_number = id_number  # Unique to Employee
        self.department = department  # Unique to Employee

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department











