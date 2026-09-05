#a program that will tell whether the given number is divisible by both 3 and 6.
num = int(input("Enter your number:"))

if(num%3==0 and num%6==0):
    print("The number is divisible by 3 and 6.")
else:
    print("The number is not divisible by 3 and 6.")
