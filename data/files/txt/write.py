import os


def search(f_name):
    print("Searching...")
    sections = []
    books = []
    with open(f_name) as file:
        for line in file:
            if line.startswith("Section"):
                sections.append(line.strip().split(":")[1])
            else:
                books.append(line.strip())

    print("Done!")

    return sections, books


def save(f_name, data):
    sections, books = data
    print("Saving...")
    with open(f_name, "w") as file:
        file.write("Sections: {}\n".format(sections))
        file.write("Books: {}\n".format(books))
    print("Done")


def run():
    data = search("books.txt")
    save("section-books.txt", data)


run()
