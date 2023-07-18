def box_m(word):
    box = "* {} *".format(word)
    print("*" * (len(box)))
    print(box)
    print("*" * (len(box)))


def lower_c(word):
    return str.lower(word)


def upper_c(word):
    return str.upper(word)


def mirror(word):
    str_l = len(word)
    return word[str_l::-1]


def repeat(word):
    print("How many time would you like the word to be displayed ?")
    how_many = int(input())
    while how_many > 0:
        if how_many % 2 > 0:
            print(upper_c(word))
        else:
            print(lower_c(word))
        how_many -= 1


print("Enter a word ")
word = input(str())

print("Select number from menu: ")
print("1. Display your word in a box")
print("2. Display your word in lower-case")
print("3. Display your word in upper-case")
print("4. Display your word mirrored")
print("5. Select how many times repeat your word alternating upper-case and lower-case")

menu_n = int(input())


def run():
    if menu_n == 1:
        print(box_m(word))
    elif menu_n == 2:
        print(lower_c(word))
    elif menu_n == 3:
        print(upper_c(word))
    elif menu_n == 4:
        print(mirror(word))
    elif menu_n == 5:
        print(repeat(word))
    else:
        print("Wrong number selected")


run()