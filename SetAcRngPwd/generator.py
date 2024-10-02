import random
import string

def generatorPassword(len : int = 8):
    characters = string.ascii_letters + string.digits

    excluded_characters = '0oOlI1'  
    for char in excluded_characters:
        characters = characters.replace(char, '')
    
    password = ''.join(random.choices(characters, k = len))
    return password