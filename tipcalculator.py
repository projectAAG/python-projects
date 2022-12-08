print("Welcome to the tip Claculator !")
bill = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give ? 10 , 12 , or 15 "))
total_bill = bill * tip / 100 + bill
people = int(input("How many people to split the bill?"))
#split_bill = round(total_bill / people , 2)
split_bill = "{:.2f}".format(total_bill / people)
print (f"each person would be paying a total amount of ${split_bill} Thank you for choosing AAG Motors")
