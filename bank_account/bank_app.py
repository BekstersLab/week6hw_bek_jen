from account import Account

# INSTANTIATION
# creation of objects (eg. lisa_account) which are instances of the Account class for various characters
# instantiation involves calling the constructor of the class

lisa_account = Account('Lisa', 'Savings', 19740845, 100,'Lisa', 'Marie', 'Simpson', 8)
print(lisa_account)

bart_account = Account('Bart', 'Savings', 34866290,20, 'Bartholomew', 'JoJo', 'Simpson', 10)
print(bart_account)

maggie_account = Account('Maggie', 'Savings', 73408236,10, 'Margaret', 'Evelyn', 'Simpson', 1)
print(maggie_account)

homer_account = Account('Homer', 'Current', 75297806,2550, 'Homer', 'Jay', 'Simpson', 36)
print(homer_account)

marge_account = Account('Marge', 'Current', 65886439,850, 'Marjorie', 'Jacqueline', 'Simpson', 34)
print(marge_account)

bob_account = Account('Sideshow Bob', 'current', 87640897,200, 'Robert', 'Underdunk', 'Terwilliger', 35)
print(bob_account)

# METHOD CALLS
# operations on objects (eg. lisa_account) such as get_balance(), get_firstname() etc demonstrate method calls that
# act on the internal state of the objects or return information about them

# ******** Lisa's Account ********
lisa_balance = lisa_account.get_balance()
print(f"Lisa's balance is ${lisa_balance}")  # Lisa's _balance is $100

lisa_account.deposit(20)
lisa_balance = lisa_account.get_balance()
print(f"Lisa's new balance is ${lisa_balance}")  # Lisa's new _balance is $120

firstname = lisa_account.get_firstname()
print(firstname)  # Lisa

# this doesn't work because it is private
# lastname = lisa_account.last_name
# print(lastname)

# this now works - getter modifies data before returning it
lastname = lisa_account.get_lastname()
print(lastname)  # Simpson

lisa_age = lisa_account.get_age()
print(f"Lisa is {lisa_age} years old!")  # Lisa is 8 years old!

lisa_account.set_lastname("Van Houten")
print(f"Lisa's old lastname was {lastname} and her new lastname is {lisa_account.get_lastname()}")
# Lisa's old lastname was Simpson and her new lastname is Van Houten

# ******** Bart's Account ********
bart_balance = bart_account.get_balance()
print(f"Bart's bank account opening balance is ${bart_balance}")  # Bart's bank account opening balance is $20

bart_account.withdraw(10)
bart_balance = bart_account.get_balance()
print(f"Bart's balance after making a withdrawal is ${bart_balance}")  # Bart's balance after making a withdrawal is $10

bart_account.deposit(50)
bart_balance = bart_account.get_balance()
print(f"Bart's balance after depositing his birthday money is ${bart_balance}")
# Bart's balance after depositing his birthday money is $60

print(f"Bart's middle name is {bart_account.get_middlename()} and he is {bart_account.get_age()} years old")
# Bart's middle name is JoJo and he is 10 years old

# STILL TO LOOK AT....
# Inheritance
# Account class is base class (superclass)
# Create 'SavingsAccount' class that inherits from Account - could be used to apply interest to savings account only?

# Polymorphism?



