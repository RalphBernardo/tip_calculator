from optparse import OptionParser

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
    parser.add_option("-m", "--meal", dest="meal", type="float", help="enter the cost of meal without tax")
    parser.add_option("-x", "--tax", dest="tax", type="float", help="enter the tax rate")
    parser.add_option("-t", "--tip", dest="tip", type="float", help="enter the tip percentage", default=15.0)
    (options, args) = parser.parse_args()

    if not options.meal:
        parser.error("You must enter your meal cost without tax.")
    if not options.tax:
        parser.error("You must enter the tax rate.")

    meal_info = calculate_costs(options.meal, options.tax,
                                    options.tip)

    print "Your meal cost $%.2f" % meal_info['meal'] + "."

    print "The tax on your meal is $%.2f" % meal_info['tax_value'] + "."

    print "Tipping at a rate of {0}%, you tipped ${1:.2f} on your meal.".format(int(options.tip), meal_info['tip_value'])

    print "Your meal's total cost is $%.2f" % meal_info['total'] + "."

if __name__ == '__main__':
    main()