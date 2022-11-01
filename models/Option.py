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

    def getRisk(self):
        risk = 0
        risk += self.getVolatilityRisk()
        risk += self.getComparisonRisk()
        return risk

    def getVolatilityRisk(self):
        volatility = self.volatility
        if volatility < 0.1:
            return 5
        elif volatility < 0.15:
            return 3
        elif volatility < 0.2:
            return 0
        else:
            return -5

    def getComparisonRisk(self):
        exercise = self.exercise_price
        alternative = self.altEstimation
        difference = abs(alternative - exercise)
        realPrice = self.stock.getStock().info["previousClose"]
        if difference < (realPrice/10):
            return 5
        elif difference < ((realPrice/10)*2):
            return 3
        else:
            return -3