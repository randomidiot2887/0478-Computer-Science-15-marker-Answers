#Functions
def Cuboid(base, debth, height):#For cylinder
    return base, debth, height

def Trangular_prism(base, debth, height):#For tranngular psism
    bdh = base * debth * height
    return bdh * 0.5

def Sphere(radius):#For sphere
    Pi = 3.142
    return radius * radius * radius * Pi * (4/3)


while True:
    print("Welcome to volume calculator 2000")
    print("Input 'C' to calculate volume of Cuboid")
    print("Input 'T' to calculate volume of Trangular Prism")
    print("Input 'S' to calculate volume of Sphere")
    print("Input 'E' to exit")
    option = input("Input option: - ")
    match option:
        case 'C':
            b = float(input("Base: - "))
            d = float(input("Debth: - "))
            h =  float(input("Height: - "))
            v = round(Cuboid(b, d, h), 2)
            print(f"Volume of cuboid is {v}m3")
        case 'T':
            b = float(input("Base: - "))
            d = float(input("Debth: - "))
            h = float(input("Height: - "))
            v = round(Trangular_prism(b, d, h), 2)
            print(f"Volume of Tranguler Prism is {v}")
        case 'S':
            r = float(input("Input radius: - "))
            v = round(Sphere(r), 2)
            print(f"Volume of Sphere is {v}")
        case 'E':
            print("Exiting"); break
        case _: print("Invalid Input")
