"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
    else:
        return
    do_something(n - 1)

# TODO: 3. write down what you think the output of this will be,
# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)
# TODO: 5. fix do_something() so that it works the way it probably should :)

def outside_in(x):
    if x != "":
        print(x[0], end=" ")
        outside_in(x[-1:0:-1])
    else:
        return
# outside_in("A Toyota's a Toyota")

def pyramid(n):
    if n > 0:
        return pyramid(n-1) + n
    return 0

print(pyramid(6))