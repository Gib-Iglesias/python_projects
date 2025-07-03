# -*- coding: utf-8 -*-

#Gibran´s Final Code
import random
import string

def get_password(length, types):
    characters = ""
    if "numbers" in types:
        characters += string.digits
    if "letters_lowercase" in types:
        characters += string.ascii_lowercase
    if "letters_uppercase" in types:
        characters += string.ascii_uppercase
    if "symbols" in types:
        characters += string.punctuation
    if not characters:
        raise ValueError("Debe especificar al menos un tipo de caracter para la contraseña.")

    password = random.choices(characters, k=length)
    return "".join(password)

if __name__ == '__main__':
    password_1 = get_password(50, ["numbers", "letters_lowercase", "letters_uppercase", "symbols"])
    print(f"Contraseña 1: {password_1}")

    password_2 = get_password(20, ["numbers", "letters_uppercase", "symbols"])
    print(f"Contraseña 2: {password_2}")

    password_3 = get_password(12, ["numbers", "letters_lowercase"])
    print(f"Contraseña 3: {password_3}")


#################################################################################################################################################

#Adrian´s Code
import random
import string

def generate_password(length):
    nums = string.digits
    letters_uppercase = string.ascii_uppercase
    letters_lowercase = string.ascii_lowercase
    symbols = string.punctuation

    complete_string = nums + letters_uppercase + letters_lowercase + symbols
    password = random.choices([i for i in complete_string], k=length)
    return "".join(password)

if __name__ == '__main__':
    password1 = generate_password(15)
    print(password1)
