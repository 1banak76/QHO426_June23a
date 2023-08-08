import os


def search(f_name):
    print("Searching...")
    with open(f_name) as file:
        for line in file:
            location = line.strip()
            print(f"Looked in {location}")
    print("...Done")


def run():
    path = os.getcwd()
    search(f"{path}/locations.txt")


run()