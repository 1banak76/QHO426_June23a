# Initialises empty dictionary
d = {}
d2 = dict()
# Initialise non-empty dictionary
phonebook = {"Thomas": 774344310, "Ruud": 73434315151, "July": 774591029}
# Print individual elements
name = input("Who you gonna call? ")
if name in phonebook:
    print(f"Calling .....{phonebook[name]}")
else:
    print(f"No number for {name}")

# Zipping two lists together into a dictionary
names = []



#Traversing Dictionaries - accessing keys/values
for thing in people:
    print(thing)
for thing in people.values():
    print(thing)
for v, k in people.items():
    print(f"Person {k} is {v} years old")