def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction: ")
    lista = directions()

    for index in range(len(lista)):
        print("{}: {}".format(index, lista[index]))
    user_s = int(input("Please enter a direction: "))
    return lista[user_s]


def run():
    route = []
    print("Working out escape route ...")
    for i in range(0, 5):
        choice = menu()
        route.append(choice)
    print("Escape route: ", route)


run()