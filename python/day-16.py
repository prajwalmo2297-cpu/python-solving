#program that determines the weather based on user-provided temperature and humidity.
temp = int(input("Enter the temprature:"))
humi = int(input("Entre the humidity:"))

if temp>=30 and humi>=90:
    print("The whether is Hot and Humid.")
if temp>=30 and humi<90:
    print("The whether is Hot.")
if temp<30 and humi>=90:
    print("The whether is Cool and Humid.")
else:
    print("The whether is Cool.")
