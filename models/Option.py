import string
import datetime
from enum import Enum
from random import random


class Option:
    def __init__(self, stock, maturity_date, exercise_price, optionType, volatility) -> None:
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
        #self.altEstimation = self.getAltEstimation()
        self.ranking = self.getRank()

    def getAltEstimation(self):
        #todo: Query for yfinance's estimate
        estimation = self.stock.analysis['Growth']
        return estimation

    def getRisk(self):
        risk = 0
        risk += self.getVolatilityRisk()
        return random()

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
