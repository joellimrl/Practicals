from prac07.car import Car

def main():
    print("Let's drive!")
    userCar = Car(input("Enter your car name: "), 100)
    menu(userCar)
    print("\nGood bye {}'s driver".format(userCar.name))

def menu(userCar):
    choice = ""
    while choice.upper() != "Q":
        print("\n{}, fuel = {}, odo = {}".format(userCar.name,userCar.fuel,userCar.odometer))
        print("Menu:\nd) drive\nr) refuel\nq) quit")
        choice = input("Enter your choice:")
        if choice.upper() == "D":
            drive(userCar)
        elif choice.upper() == "R":
            refuel(userCar)
        elif choice.upper() == "Q":
            continue
        else:
            print("Invalid choice")

def drive(userCar):
    while True:
        try:
            distance = int(input("How many km do you wish to drive? "))
            if distance < 0:
                print("Distance must be >= 0")
                continue
            newDistance = userCar.drive(distance)
            if newDistance == distance:
                print("The car drove {}km".format(distance))
            else:
                print("The car drove {}km and ran out of fuel.".format(newDistance))
            break
        except ValueError:
            print("That is not a valid number. Please enter a whole number")

def refuel(userCar):
    while True:
        try:
            units = int(input("How many units of fuel do you want to add to the car? "))
            if units < 0:
                print("Fuel amount must be >= 0")
                continue
            userCar.add_fuel(units)
            print("Added {} units of fuel.".format(units))
            break
        except ValueError:
            print("That is not a valid number. Please enter a whole number")

main()