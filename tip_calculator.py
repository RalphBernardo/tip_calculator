meal = 44.53
tax = 0.0675
tip = 0.15

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "Your meal cost $%.2f" % meal + "."

print "The tax on your meal is $%.2f" % tax_value + "."

print "You tipped $%.2f" % tip_value + " on your meal."

print "Your meal's total cost is $%.2f" % total + "."