# -*- coding: utf-8 -*-
import random
import string


#Adrian´s Code
def generate_password(length):
    nums = string.digits
    letters_uppercase = string.ascii_uppercase
    letters_lowercase = string.ascii_lowercase
    symbols = string.punctuation

    complete_string = nums + letters_uppercase + letters_lowercase + symbols
    password = random.choices(complete_string, k=length)
    return "".join(password)


if __name__ == '__main__':
    password1 = generate_password(15)
    print(password1)
