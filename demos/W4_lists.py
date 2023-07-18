#Declare empty list
bleh = []
meh = list()
#Declare non-empty list
yummy = ["chocolate", "pizza", "doughnuts", "subway"]
#Print entire list
print(yummy)
#Print a single item
print(yummy[0])
print(yummy[-1])
#Print some items off the list
print(yummy[0:4:2])
print(yummy[::2])
#printing in reverse
print(yummy[::-1])

print (bleh)
bleh.append("spinach")
bleh.append("brocolli")
bleh.append("aubergine")
bleh.append("pesto")
print(bleh)
#Add items to a list(multiple items)
bleh.extend(["liver", "bigos", "tomatoes"])
print(bleh)
#Remove items
bleh.remove("brocolli")
print(bleh)

#insert items as specific positions
bleh.insert(1, "carrot")
print(bleh)
bleh.insert(4, "cabbage")
print(bleh)
#Remove items by index
bleh.pop(3)
bleh.pop(5)

#Mutate your list
yummy[2] = "pancakes"
print(yummy)
#Check a list for a particular data type/traverse a list
lista = ["Fred", 56, True, 99.4, "Potato", False, 82]
sum = 0
for item in lista:
    if isinstance(item, int):
        sum += item
print(sum)