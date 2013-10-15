from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--meal", dest="meal", type="float", help="enter the cost of meal without tax")
parser.add_option("-x", "--tax", dest="tax", type="float", help="enter the tax rate")
parser.add_option("-t", "--tip", dest="tip", type="float", help="enter the tip percentage", default=15.0)

(options, args) = parser.parse_args()
if not options.meal:
    parser.error("You must enter your meal cost without tax.")
if not options.tax:
    parser.error("You must enter the tax rate.")

meal = options.meal
tax = options.tax/100
tip = options.tip/100

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "Your meal cost $%.2f" % meal + "."

print "The tax on your meal is $%.2f" % tax_value + "."

print "Tipping at a rate of {0}%, you tipped ${1:.2f} on your meal.".format(int(100*tip), tip_value)

print "Your meal's total cost is $%.2f" % total + "."