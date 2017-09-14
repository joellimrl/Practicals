from prac08.unreliable_car import UnreliableCar

def main():
    lousyCar = UnreliableCar("Unreliable", 100, 50)
    print(lousyCar)
    for i in range(0,10):
        lousyCar.drive(10)
        print(lousyCar)

main()