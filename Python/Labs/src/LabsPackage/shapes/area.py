import math

def circle(radius):
    return(f"{((radius ** 2) * math.pi):.2f}")


def rectangle(side1, side2):
    return(f"{(side1 * side2):.2f}")


def square(side):
    return(f"{side ** 2:.2f}")


def triangle(side1, side2):
    return(f"{(side1 * side2) * .5:.2f}")
