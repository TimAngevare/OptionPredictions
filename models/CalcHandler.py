from datetime import date
from dateutil.relativedelta import relativedelta

def getOptions(stock):
    """
    Calculates and generates multiple possible options and their values
    @param stock: the stock for which the options should be generated
    @return: the list off all options created
    """
    result = []
    periods = ["1mo","6mo","1y","2y","3y"]
    for period in periods:
        price = stock.calc_future_price(period)
        volatility = stock.calc_volatility(period)
        maturityDate = getMaturity(period)
        altEstimate = stock.analysis['Growth']

        if price > 0:
            optionType = "call"
        else:
            optionType = "put"

        option = option(stock, maturityDate,price,optionType, volatility)

        result.append(option)

    return result

def rankOptions(options):
    """
    Sorts out all riskiest options and orders the top five
    @param options: a list of all created options
    @return: the list of options with the best five options
    """

    while len(options) > 5:
        lowest = options.get(0)
        for option in options:
            if option.ranking < lowest.ranking:
                lowest = option
        options.remove(lowest)
    """for x in range(0,4):
        option = options.get(x)
        for y in range(x,4):
            if options.get(y).ranking > option.ranking:
               option = options.get(y)
    """
    options.sort(key=rank)
    return options

def rank(e):
    return e.ranking

def getMaturity(period):
    """
    Returns the date of the according maturity of the option
    @param period gives the timeframe for which the stock is being analyzed for
    """
    if period == "2wk":
        return date.today() + relativedelta(weeks=+2)
    elif period == "1mo":
        return date.today() + relativedelta(months=+1)
    elif period == "3mo":
        return date.today() + relativedelta(months=+3)
    elif period == "6mo":
        return date.today() + relativedelta(months=+6)
    elif period == "1y":
        return date.today() + relativedelta(years=+1)
    elif period == "2y":
        return date.today() + relativedelta(years=+2)
    elif period == "3y":
        return date.today() + relativedelta(years=+3)
    else:
        raise TypeError("Invalid period given")