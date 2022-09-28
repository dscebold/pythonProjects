def power(x,y):
    if(y == 0):
        return 1
    elif(y == 1):
        return x
    else:
        return x * power(x, (y-1))


def cat_ears(n):
    if n== 0:
        return 0
    return 2 + cat_ears((n-1))


def alien_ears(n):
    if(n == 0):
        return 0
    elif(n % 2 == 0):
        return 3 + alien_ears((n-1))
    return 2 + alien_ears((n-1))


def main():
    print(alien_ears(0))
    print(alien_ears(1))
    print(alien_ears(2))
    print(power(4,0))
    print(power(4,1))
    print(power(4,2))
    print(power(4,3))
    print(power(4,4))


if __name__ == '__main__':
    main()
