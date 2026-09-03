#a program that will take user input of cost price and selling price and determine whether it’s a loss or a profit.
cost = int(input("Enter your cost:"))
income = int(input("Enter your income:"))

if cost<income:
    profit = income - cost
    profitper = ((income-cost)/cost)*100
    print(f"The business made a profit of {profit}\nThe increase in sales is {profitper}%")
else:
    loss = cost - income
    lossper = ((cost - income)/cost)*100
    print(f"The business had a loss of {loss}\nThe decrease in sales is {lossper}%")
