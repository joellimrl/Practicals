from prac08.silver_service_taxi import SilverServiceTaxi
from prac08.taxi import Taxi

def main():
    taxis = [Taxi("Prius",100),SilverServiceTaxi("Limo",100,2),SilverServiceTaxi("Hummer",200,4)]
    mainMenu(taxis)

def mainMenu(taxis):
    print("Let's drive!")
    totalBill = 0.0
    choice = "C"
    totalDistance = 0
    while True:
        if choice.upper() == "C":
            print("Taxis available:")
            taxiChoices(taxis)
            while True:
                try:
                    currentTaxi = taxis[int(input("Choose Taxi:"))]
                    break
                except ValueError:
                    print("Please enter the number in front of the choice to choose that taxi!")
                except IndexError:
                    print("Please enter a valid number from the available choices!")
        elif choice.upper() == "D":
            while True:
                try:
                    distance = int(input("Drive how far? "))
                    break
                except ValueError:
                    print("Please enter a valid number!")
            currentTaxi.start_fare()
            totalDistance += currentTaxi.drive(distance)
            print("Your {} trip cost you ${}".format(currentTaxi.name, currentTaxi.get_fare()))
            totalBill += currentTaxi.get_fare()
        elif choice.upper() == "Q":
            print("Total trip cost: ${:.2f}".format(totalBill))
            break
        else:
            print("That's not a valid choice! Please enter a valid choice from the menu.")
        print("Bill to date: ${:.2f}".format(totalBill))
        print("Total distance driven: {}km".format(totalDistance))
        choice = input("Q)uit, C)hoose taxi, D)rive\n>>>")
    print("Taxis are now:")
    taxiChoices(taxis)

def taxiChoices(taxis):
    x = 0
    for each in taxis:
        print("{} - {}".format(x, each))
        x += 1

main()