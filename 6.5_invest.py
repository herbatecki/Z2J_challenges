

def invest(amount, rate, years):
    amount = 100.00
    rate = .05
    years = range(1, 5)
    for year in years:
        amount += (amount * rate) # w nawiasie wartość rocznych odsetek (się zwiększa po roku, dwóch, trzech itd.) dodawana do kapitału początkowego (jest stały)
        print(f"year {year}: ${amount:,.2f}")

invest(100, .05, 4)

print("")

def invest_user(amount, rate, years):
    amount = float(input(f"Please give your principal deposit: "))
    rate = float(input(f"Please give your potential rate of return: "))
    years = range(int(input(f"Please give number of years of investment: ")))
    print("")
    check_years = print(f"real Python indices of given number of years by user is {list(years)}")
    print("")
    for year in years:
        amount = amount + (amount * rate)
        print(f"year {year + 1}: ${amount:,.2f}")

invest_user(float, float, range) # possible to give as a third parameter also 'int', 'list', etc
