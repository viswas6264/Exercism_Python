def exchange_money(budget, exchange_rate):
    one_usd=1/exchange_rate
    exchanged_money=one_usd*budget
    return exchanged_money
    
def get_change(budget, exchanging_value):
    return budget-exchanging_value
    
def get_value_of_bills(denomination, number_of_bills):
    return denomination*number_of_bills
    
def get_number_of_bills(amount, denomination):
    return amount//denomination
    
def get_leftover_of_bills(amount, denomination):
    return amount%denomination
    
def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_rate=exchange_rate*(1+spread/100)
    exchanged= exchange_money(budget,actual_rate)
    total_bill=get_number_of_bills(exchanged,denomination)
    return int(get_value_of_bills(denomination,total_bill))