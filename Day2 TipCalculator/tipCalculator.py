print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))

tip = int(input("what percentage tip would you like to give? 10,12, or 15? "))

people = int(input("How many people to split the bill? "))

total_bill = (total_bill*((tip/100)+1))

each_pay = round(total_bill/people, 2)

print(f"Each person should pay: ${each_pay}")


