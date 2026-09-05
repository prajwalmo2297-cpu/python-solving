#a program that will check whether the number is an Armstrong number or not.
num = int(input("Enter the number:"))

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
