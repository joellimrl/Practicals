import random

STARTING_POPULATION = 1000

def main():
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: {}".format(STARTING_POPULATION))
    population = STARTING_POPULATION
    for year in range(1,11):
        print("\nYear {}\n*****".format(year))
        bornGophers = randomise(population,0.1,0.2)
        deadGophers = randomise(population,0.05,0.25)
        print("{} gophers were born. {} died.".format(bornGophers,deadGophers))
        population += bornGophers - deadGophers
        print("Population: {}".format(population))

def randomise(population,lower,upper):
    return random.randint(int(population * lower), int(population * upper))

main()