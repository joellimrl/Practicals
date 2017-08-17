"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALL = "abcdefghijklmnopqrstuvwxyz"

word_format = input("Enter the word format here (% for consonant, # for vowel and * for either) e.g %#*%\nYou may also choose to automate it by typing random: ")
if word_format.lower() == "random":
    word_format = ""
    for i in range(random.randint(3,10)):
        word_format += random.choice("#%*")
    print("The randomised word format is:",word_format)

word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(ALL)
    elif kind in ALL:
        word += kind

print("Your random word is:",word)