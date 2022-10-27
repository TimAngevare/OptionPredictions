from datetime import date
from dateutil.relativedelta import relativedelta
def getOptions(stock):
    result = []
    periods = ["2wk","1mo","3mo","6mo","1y","2y","3y"]
    for period in periods:
        price = stock.calc_future_price(period)
        volatility = stock.calc_volatility(period)
        maturityDate = getMaturity(period)
        result.append(option(maturityDate))



    six_months = date.today() + relativedelta(months=+6)
    return result


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