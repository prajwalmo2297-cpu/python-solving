#a program to find the volume of a cylinder. Also, find the cost when the cost of 1 litre of milk is 40 Rs.
rad = int(input("Enter the radius of cylinder in cm:"))
hei = int(input("Enter the height of cylinder in cm:"))

volume = rad*hei*3.142
print(f"The volume of cylinder is {volume} cm³")

price = (volume/1000)*40
print(f"The price of {volume/1000} liters milk is {price}")
