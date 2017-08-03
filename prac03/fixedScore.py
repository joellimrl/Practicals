"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(calculateScore(score))

def calculateScore(score):
    if score < 0 or score > 100:
        return"Invalid score"
    elif score < 50:
        return"Bad"
    elif score < 90:
        return"Passable"
    elif score >= 90:
        return "Excellent"

main()