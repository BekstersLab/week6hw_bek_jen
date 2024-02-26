# import Cat and SpecialNeedsCat from cat_class.py file
from cat_class import Cat, SpecialNeedsCat

# Cat at https://www.bathcatsanddogshome.org.uk/
# create an instance of the Cat class (instantiation)
# pepsi is an object of the Cat class
pepsi = Cat('Pepsi', 'Female', 'Domestic Shorthair Cross', 12, 'BC29717')

# printing attributes (variables that belong to object) of pepsi object
print(f"Name: {pepsi.name}")
print(f"Identifier: {pepsi.id_number}")
print(f"Sex: {pepsi.sex}")
print(f"Breed: {pepsi.breed}")

# calling a method of pepsi object (function that belongs to object)
print(pepsi.introduction())

# add personality traits to pepsi object by calling its method
pepsi.add_personality_trait('sweet')
pepsi.add_personality_trait('loving')
pepsi.add_personality_trait('friendly')
# prints as a string due to ', '.join method on a list
print(pepsi.print_personality())

print('*' * 25)

# INHERITANCE
# create an instance of the SpecialNeedsCat class (subclass/child of Cat class)
# inheritance - SpecialNeedCat inherits functionality of Cat and is extended with medical_history etc.
# My old cat Barry (she), adopted in old age!
barry = SpecialNeedsCat('Barry', 'Female', 'Calico', 17, 'BC29745',
                        'Diabetic, arthritis in hips',
                        'Shellfish allergy, wet food twice daily',
                        'Needs food mashing due to only having two teeth')

# printing attributes of barry object
# some inherited from Cat eg. name, sex, breed, age, id_number
# some inherited from SpecialNeedsCat eg. medical_history, dietary_preferences, special_needs
print(f"Name: {barry.name}")
print(f"Identifier: {barry.id_number}")
print(f"Sex: {barry.sex}")
print(f"Breed: {barry.breed}")
print(f"Medical History: {barry.medical_history}")
print(f"Dietary Preferences: {barry.dietary_preferences}")
print(f"Special Needs: {barry.special_needs}")

# calling methods of barry object from SpecialNeedsCat sub class (child) to add and print medications
barry.add_medication('Insulin', '4 units', 'twice daily')
barry.add_medication('Meloxicam', '0.5mg/ml oral suspension', 'once daily')
barry.print_medications()

# calling introduction method inherited from Cat class
print(barry.introduction())
# add personality traits to barry object by calling its method
barry.add_personality_trait('aloof')
barry.add_personality_trait('lazy')
barry.add_personality_trait('greedy')
print(barry.print_personality())

print('*' * 25)
