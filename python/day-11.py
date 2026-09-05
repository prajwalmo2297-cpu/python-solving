#a program to find the simple interest when the value of the principal, rate of interest, and time period is given.
pri = int(input("Enter Principal Amount:"))
roa = int(input("Enter Rate of Interest:"))
tp = int(input("Enter Time period:"))

SI = (pri*roa*tp)/100
print(f"Your Simple Interest over {tp} years is: {SI} ")
