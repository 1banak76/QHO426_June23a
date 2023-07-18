word = input("Enter a word:")
#iterate through every character in a string
for letter in word:
    if ord(letter) >= 97 and ord(letter) <=122:
        print(chr(ord(letter)-32), end = "")
    else:
        print(letter, end ="")

print(word.upper())