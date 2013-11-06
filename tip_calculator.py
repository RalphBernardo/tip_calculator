from optparse import OptionParser

def meal_input(meal):
    while True:
        try:
            meal = float(meal)
        except ValueError:
            print "You must supply a number for your meal cost."
            meal = raw_input("Please enter your meal cost: ")
        else:
            return meal
            break

def tax_input(tax):
    while True:
        try:
            tax = float(tax)
        except ValueError:
            print "You must supply a number between 0 and 100 for the tax rate."
            tax = raw_input("Please enter your tax rate: ")
        else:
            return tax
            break

def tip_input(tip):
    while True:
        try:
            tip = float(tip)
        except ValueError:
            print "You must supply a positive number for your tip percentage."
            tip = raw_input("Please enter your tip percentage: ")
        else:
            return tip
            break

def calculate_costs(meal, tax, tip):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = meal * tax/100
    meal_with_tax = meal + tax_value
    tip_value = meal_with_tax * tip/100
    total = meal_with_tax + tip_value
    meal_info = dict(meal=meal, tax=tax, tip_value=tip_value, tax_value=tax_value, total=total)
    return meal_info

def main():
    parser = OptionParser()
    parser.add_option("-m", "--meal", dest="meal", help="enter the cost of meal without tax")
    parser.add_option("-x", "--tax", dest="tax", help="enter the tax rate")
    parser.add_option("-t", "--tip", dest="tip", help="enter the tip percentage", default=15.0)
    (options, args) = parser.parse_args()

    if not options.meal:
        parser.error("You must enter your meal cost without tax.")
    if not options.tax:
        parser.error("You must enter the tax rate.")

    meal = meal_input(options.meal)

    tax = tax_input(options.tax)

    tip = tip_input(options.tip)

    meal_info = calculate_costs(meal, tax, tip)

    print "\nYour meal cost is $%.2f" % meal_info['meal'] + "."

    print "The tax on your meal is $%.2f" % meal_info['tax_value'] + "."

    print "Tipping at a rate of {0}%, you tipped ${1:.2f} on your meal.".format(int(tip), meal_info['tip_value'])

    print "Your meal's total cost is $%.2f" % meal_info['total'] + ".\n"

if __name__ == '__main__':
    main()