def main():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))
    print("The first number is {}.\nThe last number is {}.".format(numbers[0],numbers[-1]))
    print("The smallest number is {}.\nThe largest number is {}.".format(min(numbers),max(numbers)))
    print("The average of the numbers is {}.".format(sum(numbers)/len(numbers)))

main()