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

    def calc_future_price(self):
        return 0
