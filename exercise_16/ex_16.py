from ex_16_classes import Person, Employee

employee_1 = Employee('Robert', 'Edward', 'Jones', 'robert.jones@gmail.com',
                      'EM4505', 'sales')

firstname = employee_1.get_firstname()
middlename = employee_1.get_middlename()
lastname = employee_1.get_lastname()
email = employee_1.get_email()
id = employee_1.get_id_number()
department = employee_1.get_department()

print(f"{firstname} {middlename} {lastname} works in the {department} department")