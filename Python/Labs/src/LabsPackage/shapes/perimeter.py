import math

def circle(radius):
    return(f"{(radius * 2 * math.pi):.2f}")


def rectangle(side1, side2):
    return (f"{((side1 * 2) + (side2 * 2)):.2f}")


def square(side):
    return(f"{side * 4:.2f}")


def triangle(side1, side2, side3):
    return(f"{side1 + side2 + side3:.2f}")
