"""
Write code for a function that takes two lists:
a list of names
a corresponding list of ages
(That is, elements at the same list index represent the same person.)
The function should return the name of the oldest person in the list.
(Return the first name if multiple people have the same oldest age.)
"""

def findOldest(names,ages):
    oldest = max(ages)
    return names[ages.index(oldest)]

names = ['bob','john','mary']
ages = [2,22,4]
print(findOldest(names,ages))