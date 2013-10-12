meal = float(raw_input("Enter the cost of your meal before tax: "))
tax = float(raw_input("Enter the tax rate as a percentage: "))/100
tip = float(raw_input("Enter your tip as a percentage: "))/100

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "Your meal cost $%.2f" % meal + "."

print "The tax on your meal is $%.2f" % tax_value + "."

print "You tipped $%.2f" % tip_value + " on your meal."

print "Your meal's total cost is $%.2f" % total + "."