from prac08.silver_service_taxi import SilverServiceTaxi

def main():
    fancyTaxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    print(fancyTaxi)
    fancyTaxi.drive(18)
    print("{:.2f}".format(fancyTaxi.get_fare()))

main()