

def get_scores():
    best_score = 0
    while True:
        try:
            num_students = int(input("Total number of students: ")) # try catch to get number of students, will only take ints and exits while loop when it gets a number
        except ValueError:
            print("Type a Number")
        else:
            break
    nums = input(f"Enter {num_students} scores: ") # gets the scores and splits them into a list
    scores = nums.split(" ", -1)
    if len(scores) < num_students:
        num_students = len(scores)
    for i in range(num_students): # checks if each object in array is numeric, if it is it casts it to int, if it isn't asks you to give it a number until you do 
        if scores[i].isnumeric():
            scores[i] = int(scores[i])
        else:
            while True:
                try:
                    scores[i] = int(input(f"Score {i+1} is not a number, please type a number: "))
                except ValueError:
                    print("Type a Number")
                else:
                    break
    for i in range(num_students): # iterates through scores to find highest score
        if scores[i] > best_score:
            best_score = scores[i]
    for i in range(num_students): # determines grade of each score and prints it
        if scores[i] >= best_score - 10:
            print(f"Student {i+1} score is {scores[i]} and grade is A")
        elif scores[i] >= best_score - 20:
            print(f"Student {i+1} score is {scores[i]} and grade is B")
        elif scores[i] >= best_score - 30:
            print(f"Student {i+1} score is {scores[i]} and grade is C")
        elif scores[i] >= best_score - 40:
            print(f"Student {i+1} score is {scores[i]} and grade is D")
        else:
            print(f"Student {i + 1} score is {scores[i]} and grade is F")


get_scores()
