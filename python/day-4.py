# sum of digits entered by user
n = int(input("Enter the number of numbers you want to enter:"))
sum = 0

for i in range(1, n+1):
    num = int(input("Enter your number:"))
    sum = sum + num

print(sum)
