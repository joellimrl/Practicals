"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random


def main():
    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"
    word_format = input("Please enter the word format: ")
    while not is_valid_format(word_format):
        print("Please enter only c or v")
        word_format = input("Please enter new word format: ")
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)

def is_valid_format(word):
    for char in word:
        if char not in ("c","v"):
            return False
    return True

main()