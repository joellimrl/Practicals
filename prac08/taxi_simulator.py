from prac08.silver_service_taxi import SilverServiceTaxi
from prac08.taxi import Taxi

def main():
    taxis = [Taxi("Prius",100),SilverServiceTaxi("Limo",100,2),SilverServiceTaxi("Hummer",200,4)]
    mainMenu(taxis)

def mainMenu(taxis):
    print("Let's drive!")
    totalBill = 0.0
    while True:
        choice = input("Q)uit, C)hoose taxi, D)rive\n>>>")
        if choice.upper() == "C":
            print("Taxis available:")
            taxiChoices(taxis)
            currentTaxi = taxis[int(input("Choose Taxi:"))]
        if choice.upper() == "D":
            distance = int(input("Drive how far? "))
            currentTaxi.start_fare()
            currentTaxi.drive(distance)
            print("Your {} trip cost you ${}".format(currentTaxi.name, currentTaxi.get_fare()))
            totalBill += currentTaxi.get_fare()
        if choice.upper() == "Q":
            print("Total trip cost: ${:.2f}".format(totalBill))
            break
        print("Bill to date: ${:.2f}".format(totalBill))
    print("Taxis are now:")
    taxiChoices(taxis)

def taxiChoices(taxis):
    x = 0
    for each in taxis:
        print("{} - {}".format(x, each))
        x += 1

main()