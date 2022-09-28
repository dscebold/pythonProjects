import shapes.area as area
import shapes.perimeter as perimeter

def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    # Code to check that a valid shape has been selected
    while(True):
        try:
            shape = int(input('Shape number: '))
        except ValueError:
            print()
        else:
            break
    while shape < 1 or shape > 4:
        while(True):
            try:
                shape = int(input('Shape number (1-4): '))
            except ValueError:
                print()
            else:
                break
    return shape

def getCalc():
    while True:
        try:
            calc = int(input('Computation(Area - 1 or Perimeter - 2): '))
        except ValueError:
            print()
        else:
            break
    while (calc != 1 and calc != 2):
        try:
            calc = int(input('Enter 1 or 2: '))
        except ValueError:
            print()
    return calc
    
def main():
    while True:
        shape = selection()
        calc = getCalc()
       
        if(calc == 2):
            if(shape == 1):
                while (True):
                    try:
                        radius = float(input('Circle Radius: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                print(f"Circle perimeter = {perimeter.circle(radius)}")
            if(shape == 2):
                while (True):
                    try:
                        side1 = float(input('Rectangle Side 1: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                while (True):
                    try:
                        side2 = float(input('Rectangle Side 2: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                print(f"Rectangle perimeter = {perimeter.rectangle(side1, side2)}")
            if(shape == 3):
                while (True):
                    try:
                        side = float(input('Square Side: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                print(f"Square perimeter = {perimeter.square(side)}")
            if(shape == 4):
                while (True):
                    try:
                        side1 = float(input('Triangle Side 1: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                while (True):
                    try:
                        side2 = float(input('Triangle Side 2: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                while (True):
                    try:
                        side3 = float(input('Triangle Side 3: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                print(f"Triangle perimeter = {perimeter.triangle(side1, side2, side3)}")
        else:
            if(shape == 1):
                while (True):
                    try:
                        radius = float(input('Circle Radius: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                print(f"Circle area = {area.circle(radius)}")
            if(shape == 2):
                while (True):
                    try:
                        side1 = float(input('Rectangle Side 1: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                while (True):
                    try:
                        side2 = float(input('Rectangle Side 2: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                print(f"Rectangle area = {area.rectangle(side1, side2)}")
            if(shape == 3):
                while (True):
                    try:
                        side = float(input('Square Side: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                print(f"Square area = {area.square(side)}")
            if(shape == 4):
                while (True):
                    try:
                        side1 = float(input('Triangle Side 1: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                while (True):
                    try:
                        side2 = float(input('Triangle Side 2: '))
                    except ValueError:
                        print("Enter a number")
                    else:
                        break
                print(f"Triangle area = {area.triangle(side1, side2)}")
        
        answer = input("Continue(y/n): ").strip().lower()
        while answer != "y" and answer != "n":
            answer = input("Enter y or n : ").strip().lower()
        if answer == "n":
            print("PROGRAM DONE")
            break


if __name__ == '__main__':
    main()