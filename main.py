print("Welcome to tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12or 15? "))
total_bill += (tip_percentage / 100) * total_bill
people = int(input("How many people to split the bill? "))
share = round(total_bill / people, 2)
print(f"Each person should pay: ${share}")
