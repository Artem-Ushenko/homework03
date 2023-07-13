import random
import string


class PasswordGenerator:
    """Was created class for object Password Generator"""

    def __init__(self, length, include_uppercase, include_lowercase, include_digits, include_special_chars):
        '''Method init with some conditions for object Password Generator'''
        self.length = length #default: 8
        self.include_uppercase = include_uppercase #default: True
        self.include_lowercase = include_lowercase #default: True
        self.include_digits = include_digits #default: True
        self.include_special_chars = include_special_chars #default: True

    def generator(self):

        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        symbols = string.punctuation
        digits = string.digits
        your_password = ''

        if self.include_uppercase is True and self.include_lowercase is True and self.include_digits is True and self.include_special_chars is True:
            for item in range(self.length):
                your_password += random.choice(uppercase_letters + lowercase_letters + symbols + digits)

        print(your_password)


your_password = PasswordGenerator(8, True, True, True, True)
your_password.generator()