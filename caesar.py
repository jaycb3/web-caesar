#helpers.py
import string

'''helper methods for use with encryption functions'''

def alphabet_position(letter):
    alphabet_lc = string.ascii_lowercase
    return alphabet_lc.index(letter.lower())


def rotate_character(char, rot):
    alphabet_lc = string.ascii_lowercase
    if not char.isalpha():
        return char
    else:
        result = (alphabet_lc[(alphabet_position(char.lower())+rot) % 26])
    if char.isupper():
        return result.upper()
    else:
        return result

"""encryption function using variable rotation"""

def encrypt(text, rot):
    newtext = ""
    for char in text:
        newtext += rotate_character(char, rot)
    return newtext
