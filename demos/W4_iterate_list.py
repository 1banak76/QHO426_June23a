def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    lista = directions()

    for index in range(len(lista)):
        print("{}: {}".format(index, lista[index]))


def run():
    menu()

run()