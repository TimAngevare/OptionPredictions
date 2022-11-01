import string
import datetime
from enum import Enum
from random import random


class Option:
    def __init__(self, stock, maturity_date, exercise_price, optionType, volatility, altEstimation) -> None:
        """
        Class for a stock option
        @requires optionType to be either 'call' or 'put'
        @param stock: gives the yfinance Tracker of the selected stock
        @param maturity_date: gives the date of maturity
        @param exercise_price: gives the price for which the price is bought
        @param optionType: gives the type of option (Either CALL or PUT)
        @param volatility: gives the volatility of the stock
        """

        #Assigning all parameters
        self.stock = stock
        self.maturity_date = maturity_date
        self.exercise_price = exercise_price
        self.optionType = optionType
        self.volatility = volatility
        self.altEstimation = altEstimation
        self.ranking = self.getRisk()
        print(f"Final ranking for Maturity date {self.maturity_date}: " + str(self.ranking) + "\n")

    def getRisk(self):
        comparison_risk = self.getComparisonRisk()
        volatility_risk = self.getVolatilityRisk()
        
        print('')
        print("Volatility:")
        print(f"Volatility is {self.volatility} and given risk: {volatility_risk}")
        print(f"Risk score for comparison: {comparison_risk}")
        return  volatility_risk + comparison_risk

    def getVolatilityRisk(self):
        volatility = self.volatility
        if volatility < 10:
            return 5
        elif volatility < 15:
            return 3
        elif volatility < 20:
            return 0
        else:
            return -5

    def getComparisonRisk(self):
        exercise = self.exercise_price
        alternative = self.altEstimation
        difference = abs(alternative - exercise)
        print("")
        print("Difference to expert estimate:")
        print(f"Difference of estimates: {difference}")
        realPrice = self.stock.getStock().info["previousClose"]
        print(f"10% of current stock price is: {realPrice / 10}")
        if difference < (realPrice/10):
            return 5
        elif difference < ((realPrice/10)*2):
            return 3
        else:
            return -3