def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    lista = movements()
    for i in range(0, (len(lista)-1), 2):
        direction = lista[i]
        steps = lista[i+1]
        print(f"{direction} for {steps} steps")


run()