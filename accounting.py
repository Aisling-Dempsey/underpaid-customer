melon_cost = 1.00


def price_checker(log):
    """This function will check the log file to see if there are any pricing errors"""
    log_file = open(log)
    for line in log_file:
        order_info = line.split("|")
        customer = order_info[1]
        melons_ordered = float(order_info[2])
        paid = float(order_info[3])
        price = melon_cost * melons_ordered
        pay_difference = abs(price-paid)

        if price < paid:
            print "%s should have paid %d but they paid %d" % (customer, price, paid)
            print "They overpaid by " + str(pay_difference)
        elif price > paid:
            print "%s should have paid %d but they paid %d" % (customer, price, paid)
            print "They underpaid by " + str(pay_difference)

#returns float for difference, but only integers for variable 'paid'. Why?

    log_file.close()

price_checker("customer-orders.txt")
