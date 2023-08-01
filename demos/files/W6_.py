#open file for reading
f = open("song.txt")

#print single line
print(f.readline(), end="")
print(f.readline(), end="")

#print full content of the file
print(f.read())
#grab content of txt file and save it as a list
lista = f.readlines()
print(lista)
print(lista[2])
f.close()
g = open("song.txt", "a")
g.write("\nAnd it's everlasting, infinite\n")

g.writelines(["It goes on and on, you can't measure it\n"])