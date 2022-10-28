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
        #print(historic['Close'], len(historic['Close']))

        mean = sum(values) / len(values)
        deviation = [price - mean for price in values]
        variance = sum([dev * dev for dev in deviation]) / len(values)
        std_dev = math.sqrt(variance)

        rel_std_dev = (std_dev * 100) / mean
        
        return rel_std_dev
    
    def calc_growth_rate(self, eps_an, years):
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
            if i < 3:
                source = self.stock.balancesheet
            elif i < 5:
                source = self.stock.financials
            else:
                source = self.stock.cashflow
            
            data_gr = 0
            for j, year in enumerate(years):
                if j == len(years) - 1:
                    break
                    
                present = source[year][data]
                past = source[years[j + 1]][data]
                data_gr += ((present - past) / past)
            

            result += ((data_gr / 2) * weight)
        
        #Specific for EPS
        eps_gr = 0
        for i, eps in enumerate(eps_an):
            if i == len(years) - 1:
                break
                    
            past = eps_an[i + 1]
            eps_gr += ((eps - past) / past)
        result += ((eps_gr / 2) * 0.25)


        return result

    def get_future_price(self):
        historic = self.stock.history(start='2019-01-01', end='2021-12-31', interval='1mo')['Close']
        fc = historic[historic.notnull()]
        financial_years = self.stock.financials.keys()[:3]

        eps_an = [round(self.stock.financials[year]['Net Income Applicable To Common Shares'] / self.stock.shares['BasicShares'][year.year], 2) for year in financial_years]

        #Calculate future p/e ratio
        closes_an = [fc[ts] for ts in fc.keys() if ts.month == 12]
        closes_an.reverse()

        tot_pe = [price / eps_an[i] for i, price in enumerate(closes_an)]
        pe = round(sum(tot_pe) / len(tot_pe), 2)

        #Calculate future eps
        eps = eps_an[0] * ((1 + self.calc_growth_rate(eps_an, financial_years)) ** len(financial_years))

        return pe * eps
