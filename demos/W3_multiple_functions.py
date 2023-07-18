def display_ladder(steps):
    i = 1
    while i <= steps:
        print("| |\n***")
        i += 1


def create_ladder():
    print("How many steps remain")
    steps = int(input())
    display_ladder(steps)


create_ladder()
