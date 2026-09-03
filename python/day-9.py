# a program that takes user input of three angles and determines whether they can form a triangle.
A = int(input("Enter angle A:"))
B = int(input("Enter angle B:"))
C = int(input("Enter angle C:"))

if A+B+C == 180:
    print("The given angles form a triangle.")
