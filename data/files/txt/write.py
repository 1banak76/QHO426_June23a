import os


def search(f_name):
    print("Searching...")
    sections = []
    books = []
    with open(f_name) as file:
        for line in file:
            if line.startswith("Section"):
                sections.append(line.strip().split(":")[1])
            elif not line.startswith("Section"):
                books.append(line.strip())

    print("Done!")

    return tuple(sections) + tuple(books)


#def save(f_name,):


def run():
    path = os.getcwd()
    print(search(f"{path}/books.txt"))


run()
