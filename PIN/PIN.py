# imports pin_verification function from PIN_functions.py
from PIN_functions import pin_verification

correct_pin = 1984  # the correct PIN
# calls pin_verification function with the correct PIN. Allows you to set pin_attempts.
pin_verification(correct_pin, pin_attempts=3)

# QUERY: should pin_attempts be set here or in the PIN_functions.py file?

