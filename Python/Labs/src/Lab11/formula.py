def add(first_num, second_num):
    try:
        first_num = float(first_num)
        second_num = float(second_num)
    except ValueError:
        raise ValueError
    return first_num + second_num


def subtract(first_num, second_num):
    try:
        first_num = float(first_num)
        second_num = float(second_num)
    except ValueError:
        raise ValueError
    return first_num - second_num


def multiply(first_num, second_num):
    try:
        first_num = float(first_num)
        second_num = float(second_num)
    except ValueError:
        raise ValueError
    return first_num * second_num


def divide(first_num, second_num):
    try:
        first_num = float(first_num)
        second_num = float(second_num)
    except ValueError:
        raise ValueError
    if second_num == 0:
        raise ZeroDivisionError
    return first_num / second_num
