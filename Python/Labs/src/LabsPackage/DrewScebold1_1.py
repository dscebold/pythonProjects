
def main():
    john_tot = 0
    jane_tot = 0
    response = None
    while response != "x":
        response = vote_menu()
        if response == "v":
            add = candidate_menu()
            if add == 0:
                john_tot += 1
            elif add == 1:
                jane_tot += 1
    print("John = " + str(john_tot) + ", Jane = " + str(jane_tot) + ", Total = " + str(jane_tot + john_tot))


def vote_menu():
    print("v-vote\nx-exit")
    opt = input("Option: ").strip().lower()
    while opt != "v" and opt != "x":
        opt = input("Invalid (v/x):").strip().lower()
    return opt


def candidate_menu():
    print("0-John\n1-Jane")
    while True:
        try:
            vote = int(input("Candidate: "))
        except ValueError:
            print()
        else:
            break
    while vote != 1 and vote != 0:
        try:
            vote = int(input("Invalid (0/1): "))
        except ValueError:
            print()
    return vote


main()
