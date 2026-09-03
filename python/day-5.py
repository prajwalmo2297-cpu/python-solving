#program to tell if a given number when reversed is same
num = int(input("Enter a four-digit number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)
if original == reverse:
    print("The reversed number is the same as the original number.")
else:
    print("The reversed number is not the same as the original number.")
