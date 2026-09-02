#coverts given temprature to any for user wants
print("Select the code for your temprature:")
print("1.Celcius")
print("2.Farenheit")
print("3.Kelvin")
code = int(input("Enter your code:"))
temp = int(input("Enter the temprature:"))
print("Select the code you want to convert your temprature:")
print("C->Celcius")
print("F->Farenheit")
print("K->Kelvin")
code2 = input("Input your code for temprature:")

if code == 1 :
  if code2 == "C":
    print(f"Your temptrature is {temp}")
  elif code2 == "F":
    tempnew = (temp*(9/5))+32
    print(f"Your temprature is {tempnew}")
  else:
    tempnew = temp+ 273.15
    print(f"Your temp is {tempnew}")
    
elif code == 2 :
  if code2 == "C":
    tempnew = (temp-32)*(5/9)
    print(f"Your temptrature is {tempnew}")
  elif code2 == "F":
    print(f"Your temprature is {temp}")
  else:
    tempnew = ((temp-32)*(5/9)) + 273.15
    print(f"Your temp is {tempnew}")

else:
  if code2 == "C":
    tempnew = (temp-273.15)
    print(f"Your temptrature is {tempnew}")
  elif code2 == "F":
    tempnew = ((temp-273.15)*(9/5)+32)
    print(f"Your temprature is {tempnew}")
  else:
    print(f"Your temp is {temp}")
  
