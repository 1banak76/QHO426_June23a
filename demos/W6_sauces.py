def populate(path):
    with open(path, "w") as f:
        while True:
            sauce = input("Enter a cause you like[or \"stop\"]: ")
            if sauce.lower() == "stop":
                break
            f.write(sauce + "\n")


populate("sauces/Konrad.txt")


def reading(path):
    with open(path) as f:
        print(f.read())


reading("sauces/Jola.txt")
print("*"*20)
reading("sauces/Konrad.txt")