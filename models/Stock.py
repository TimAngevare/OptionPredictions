import math
import yfinance as yf

class Stock:
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def __str__(self) -> str:
        return self.callsign

    def calc_volatility(self, period='2wk', interval='1d'):
        historic = self.stock.history(period=period, interval=interval)
        values = [x for x in historic['Close'] if not math.isnan(x)]
        print(historic['Close'], len(historic['Close']))

        mean = sum(values) / len(values)
        deviation = [price - mean for price in values]
        variance = sum([dev * dev for dev in deviation]) / len(values)
        std_dev = math.sqrt(variance)

        rel_std_dev = (std_dev * 100) / mean
        
        return rel_std_dev
    
    #Calculate the growth rate of a stock
    #eps_an = eps' of a period / periods = the periods / bs,fc,cf = balancesheet,financials,cashflow
    def calc_growth_rate(self, eps_an, periods, bs, fc, cf):
        gr_values = {
            'Total Assets': 0.1,
            'Total Current Assets': 0.05,
            'Retained Earnings': 0.05,
            'Gross Profit': 0.2,
            'Net Income': 0.2,
            'Total Cash From Operating Activities': 0.15
        }
        result = 0

        for i, (data, weight) in enumerate(gr_values.items()):
            #Take the correct source based on the index since dicts are ordered
            if i < 3:
                source = bs
            elif i < 5:
                source = fc
            else:
                source = cf
                
            data_gr = 0
            for j, period in enumerate(periods):
                #Don't run if we cant +1 the index in the same list
                if j == len(periods) - 1:
                    break
                
                #Take present and past values of the thing
                present = source[period][data]
                past = source[periods[j + 1]][data]
                #Calculate growth rate
                data_gr += ((present - past) / past)
                
            #Add the average growth rate * weight to the total
            result += ((data_gr / 2) * weight)
            
        #Add EPS growth rate specifically
        eps_gr = 0
        for i, eps in enumerate(eps_an):
            if i == len(periods) - 1:
                break
                        
            past = eps_an[i + 1]
            eps_gr += ((eps - past) / past)
        result += ((eps_gr / 2) * 0.25)

        return result

    #Calculate the future price of a stock
    #when = period (either 1y/3y)
    def get_future_price(self, when='3y'):
        #setting the correct financial statement sheets
        #settings the correct keyword arguments for the history period
        #setting the correct list splice length for the periods
        if when == '1y':
            financials = self.stock.quarterly_financials
            bs = self.stock.quarterly_balancesheet
            cf = self.stock.quarterly_cashflow
            kwargs = {'period': '1y'}
            splice = 4
        elif when == '3y':
            financials = self.stock.financials
            bs = self.stock.balancesheet
            cf = self.stock.cashflow
            kwargs = {'start':'2019-01-01', 'end':'2021-12-31'}
            splice = 3
        else:
            print("'when' param should be 1y or 3y")
            return -1

        #Take the historic data / filter the NaN values / splice to the correct amount of periods
        historic = self.stock.history(interval='1mo', **kwargs)['Close']
        fc = historic[historic.notnull()]
        periods = financials.keys()[:splice]

        #Calculate the EPS for every period in the periods list
        eps_an = [round(financials[period]['Net Income Applicable To Common Shares'] / self.stock.shares['BasicShares'][period.year if period.year < 2022 else 2021], 2) for period in periods]

        # Calculate future p/e ratio
        #take the relevant closing prices for the periods
        if when == '1y':
            closes = [fc[ts] for ts in fc.keys() if ts.month % 3 == 0]
        elif when =='3y':
            closes = [fc[ts] for ts in fc.keys() if ts.month == 12]
        #in the correct order
        closes.reverse()

        #calculate p/e ratio for every period
        tot_pe = [price / eps_an[i] for i, price in enumerate(closes)]
        #take the average p/e ratio
        pe = round(sum(tot_pe) / len(tot_pe), 2)

        #Calculate future eps (eps * (1 + growth)_rate^periods)
        eps = eps_an[0] * ((1 + self.calc_growth_rate(eps_an, periods, bs, financials, cf)) ** len(periods))

        #return future p/e ratio * eps
        return pe * eps
