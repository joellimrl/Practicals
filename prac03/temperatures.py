"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'


def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsiusToFahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section so the program converts F to C and displays the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheitToCelsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsiusToFahrenheit(temp):
    fahrenheit = temp * 9.0 / 5 + 32
    return fahrenheit

def fahrenheitToCelsius(temp):
    celsius = 5 / 9 * (temp - 32)
    return celsius


main()