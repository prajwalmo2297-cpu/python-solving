#This is a code which compares the input ages by user and gives the oldest and yongest one
age1 = int(input("Enter the age of person 1:"))
age2 = int(input("Enter the age of person 2:"))
age3 = int(input("Enter the age of person 3:"))

if(age1>age2 and age1>age3):
    print("Person 1 is the oldest")
elif(age2>age3 and age2>age1):
    print("Person 2 is the oldest")
else:
    print("Person 3 is the oldest")

if(age1<age2 and age1<age3):
    print("Person 1 is the youngest")
elif(age2<age3 and age2<age1):
    print("Person 2 is the youngest")
else:
    print("Person 3 is the youngest")
