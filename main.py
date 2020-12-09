#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Print welcome title
print("Welcome to the tip calculator!")
#Ask user the cost of the total bill
bill = float(input("What was the total bill? $" ))
#Ask user how much percentage tip 
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
#Ask user how many people are splitting the bil
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
