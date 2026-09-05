left1 = int(input("Enter left coordinate of Rectangle 1: "))
right1 = int(input("Enter right coordinate of Rectangle 1: "))
top1 = int(input("Enter top coordinate of Rectangle 1: "))
bottom1 = int(input("Enter bottom coordinate of Rectangle 1: "))

left2 = int(input("Enter left coordinate of Rectangle 2: "))
right2 = int(input("Enter right coordinate of Rectangle 2: "))
top2 = int(input("Enter top coordinate of Rectangle 2: "))
bottom2 = int(input("Enter bottom coordinate of Rectangle 2: "))

if right1 < left2 or right2 < left1 or bottom1 > top2 or bottom2 > top1:
    print("The rectangles do not overlap.")
else:
    print("The rectangles overlap.")
