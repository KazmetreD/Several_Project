# -*- coding: utf-8 -*-

print("Choose the geometric shape number")
print("[1]Surface are of Square")
print("[2]Surface area of Triange")
print("[3]Surface area of Circle")
print("[4]Volume of Cube")
print("[5]Volume of Sphere")
choose = int(input("> "))
if choose == 1:
    edge1 = int(input("Enter the first edge: "))
    edge2 = int(input("Enter the second edge: "))
    print(edge1*edge2)
elif choose == 2:
    edge1 = int(input("Enter the first edge: "))
    height = int(input("Enter the height: "))
    print(edge1*height / 2)
elif choose == 3:
    print("[1] 3")
    print("[2] 3.14")
    pi = int(input("Which pi value do you want to use? "))
    if pi == 1:
        radius = int(input("Enter the radius: "))
        print(2*radius*3)
    elif pi == 2:
        radius = int(input("Enter the radius: "))
        print(2*radius*3.14)
elif choose == 4:
    edge1 = int(input("Enter the first edge: "))
    edge2 = int(input("Enter the second edge: "))
    edge3 = int(input("Enter the third edge: "))
    print(edge1*edge2*edge3)
elif choose == 5:
    print("[1] 3")
    print("[2] 3.14")
    pi = int(input("Which pi value do you want to use? "))
    if pi == 1:
        radius = int(input("Enter the radius: "))
        print(radius*radius*3)
    elif pi == 2:
        radius = int(input("Enter the radius: "))
        print(radius*radius*3.14)
