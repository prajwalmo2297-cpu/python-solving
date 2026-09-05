#a program that will take user input of a 4-digit number and check whether it is a narcissist number or not.
num = int(input("Enter a number: "))

original = num
power = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** power
    num = num // 10

if total == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
