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
        password=[]


        if self.include_uppercase and self.include_lowercase and self.include_digits and self.include_special_chars :
            all_ch = uppercase_letters + lowercase_letters + symbols + digits
            password = [random.choice(uppercase_letters), random.choice(lowercase_letters), random.choice(symbols), random.choice(digits)]
            password += random.sample(all_ch, self.length - len(password))

        random.shuffle(password)
        return ''.join(password)


your_password = PasswordGenerator(8, True, True, True, True)
print(f"Your password: {your_password.generator()}")
