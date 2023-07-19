def directions() -> object:
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


# print list without bracket, separated by space and comma
def run1a():
    print(', '.join(directions()))


def run1b():
    print(*directions(), sep=", ")


# print list with bracket 
def run2():
    print(directions())


# print each position of the list in new line
def run3a():
    [print(i) for i in directions()]
    

def run3b():
    print(*directions(), sep="\n")


# print list using loop
def run4():
    lista = directions()
    for i in range(0, len(lista)):
        print(lista[i])


print("Separated by space and comma, A: ")
run1a()
print("\nSeparated by space and comma, B: ")
run1b()
print("\nList with bracket: ")
run2()
print("\nIn new lines, A: ")
run3a()
print("\nIn new lines, B: ")
run3b()
print("\nUsing while loop")
run4()