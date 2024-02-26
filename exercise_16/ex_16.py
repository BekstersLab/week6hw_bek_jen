from ex_16_classes import Person, Employee

person_1 = Person('Mary', 'Alice', 'Peterson', 'mary.peterson@gmail.com')

person_firstname = person_1.get_firstname()
person_middlename = person_1.get_middlename()
person_lastname = person_1.get_lastname()
person_email = person_1.get_email()

print(f"{person_firstname} {person_lastname}'s email address is {person_email}")
# Mary Peterson's email address is mary.peterson@gmail.com


# instance of Employee class
employee_1 = Employee('Robert', 'Edward', 'Jones', 'robert.jones@gmail.com',
                      'EM4505', 'sales')

employee_firstname = employee_1.get_firstname()
employee_middlename = employee_1.get_middlename()
employee_lastname = employee_1.get_lastname()
employee_email = employee_1.get_email()
employee_id = employee_1.get_id_number()
employee_department = employee_1.get_department()

print(f"{employee_firstname} {employee_middlename} {employee_lastname} works in the {employee_department} department")
# Robert Edward Jones works in the sales department

print(f"{employee_firstname}'s ID number is {employee_id}")  # Robert's ID number is EM4505

