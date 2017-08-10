def main():
    numbers = []
    count = 1
    x = 1
    while x >= 0:
        x = int(input("Number {}: ".format(count)))
        count+=1
        if x >= 0:
            numbers.append(x)
    print("The first number is {}.\nThe last number is {}.".format(numbers[0],numbers[-1]))
    print("The smallest number is {}.\nThe largest number is {}.".format(min(numbers),max(numbers)))
    print("The average of the numbers is {}.".format(sum(numbers)/len(numbers)))

main()