# import getpass module to securely accept user input without showing it
import getpass


def check_pin(supplied_pin, correct_pin):
    # compares entered pin with correct pin and will return True if a match, otherwise False
    return supplied_pin == correct_pin


def get_pin():
    # getpass securely prompts user to enter their PIN and returns value as an integer
    return int(getpass.getpass("Enter your PIN: "))


def pin_verification(correct_pin, pin_attempts):
    # attempts to verify input PIN over specified number of attempts (set in PIN.py)
    count = 0  # initialise a counter to count PIN entry attempts
    for i in range(pin_attempts):  # loops through given PIN attempts (3 in this case)
        supplied_pin = get_pin()  # calls get_pin function to prompt user to enter their PIN
        count += 1  # increments the counter after an attempt
        if check_pin(supplied_pin, correct_pin):
            # if PIN correct, it prints following message and breaks (exits) the loop
            print(f"Correct - attempt {count} of {pin_attempts}")
            break
        else:
            # if PIN incorrect it prints following message which is updated with the attempt number
            print(f"Incorrect - attempt {count} of {pin_attempts}")
    else:
        # if loop completes without breaking this message is printed advising user that they have exceeded attempts
        print(f"You've exceeded {count} attempts. Please speak to your branch manager!")