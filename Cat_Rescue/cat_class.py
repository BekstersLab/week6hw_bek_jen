# class is called Cat (pattern/blueprint)
class Cat:
    # __init__ is a special method called the CONSTRUCTOR which starts/ends in dunderscore - it is special
    # anything inside it will be called when we create a new Cat
    # Cat is a pattern, __init__ is a method called when we instantiate a new Cat
    def __init__(self, name, sex, breed, age, id_number):
        # instance attributes are initialised with values passed to the constructor
        self.sex = sex
        self.name = name
        self.breed = breed
        self.age = age
        self.id_number = id_number
        self.personality = []  # initialising an empty list to store personality traits
        #  extend code with list for likes and return an f-string
        #  extend code with list for likes and return an f-string

    # a method for introducing the cat
    def introduction(self):
        return (f"About Me:"
                f"\nHello! My name is {self.name} and I am {self.age} years old!")

    # a method for adding personality traits
    def add_personality_trait(self, trait):
        if trait not in self.personality:
            self.personality.append(trait)

    # a method for printing the cat's personality traits, formatted with an f-string
    def print_personality(self):
        return(f"My personality can be described as {', '.join(self.personality)}!")


class SpecialNeedsCat(Cat):
    # __init__ is the CONSTRUCTOR for SpecialNeedsCat with additional parameters specific to cats with extra needs
    def __init__(self, name, sex, breed, age, id_number, medical_history, dietary_preferences, special_needs):
        # super() calls the constructor of the Cat class to initialise common attributes
        # in this case we use super() to access the __init__ method from the Cat class
        # calls the constructor function (__init__) from the parent class
        # SpecialNeedsCat now uses parent class (Cat) but adds its own attributes
        super().__init__(name, sex, breed, age, id_number)
        # initialising attributes specific to this Child class
        self.medical_history = medical_history
        self.dietary_preferences = dietary_preferences
        self.special_needs = special_needs
        self.medications = []  # initialising an empty list which will store medication details

    def add_medication(self, medication_name, dosage, timing):
        # create a tuple from the medication details
        medication_tuple = (medication_name, dosage, timing)
        # check if it already exists in medications list, if not then use append method
        if medication_tuple not in self.medications:
            self.medications.append(medication_tuple)

    def print_medications(self):
        # initialise empty list to hold strings for each medication
        medications_details = []
        # iterate over each medication in the self.medications list and store as tuple with name, dosage, timing info
        for medication in self.medications:
            # f-string accesses elements in tuple by index number
            detail = f"Medication: {medication[0]} - dosage: {medication[1]}, timing: {medication[2]}"
            # append string to the medications_details list
            medications_details.append(detail)

        # join into a single string. Use newline to separate different medications
        medications_output = "\n".join(medications_details)
        print(medications_output)








