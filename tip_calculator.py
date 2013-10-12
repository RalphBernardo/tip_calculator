import sys

meal = float(sys.argv[1])
tax = float(sys.argv[2])/100
tip = float(sys.argv[3])/100

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "Your meal cost $%.2f" % meal + "."

print "The tax on your meal is $%.2f" % tax_value + "."

print "Tipping at a rate of {0}%, you tipped ${1:.2f} on your meal.".format(int(100*tip), tip_value)

print "Your meal's total cost is $%.2f" % total + "."