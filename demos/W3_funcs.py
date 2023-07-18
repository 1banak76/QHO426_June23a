def t_area(b=1,h=1):
    #height = float(input("Enter the height: "))
    #base = float(input("Enter the base: "))
    #area = 0.5*height*base
    area = 0.5 * height * base
    #print(f"Area is {area}")
    return area

total = t_area() + t_area(h=5) + t_area(10,18)
print(f"Total area of 3 triangles is {total}")

height = float(input("Enter the height: "))
base = float(input("Enter the base: "))

t_area(base,height)
