def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    lista = movements()
    for index in range(0, len(lista)-1, 2):
        print("{} for {} steps".format(lista[index], lista[index+1]))


run()