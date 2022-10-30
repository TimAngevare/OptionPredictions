import string
import datetime
from enum import Enum

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

        #Evaluate parameters' types
        if type(maturity_date) != 'str':
            # Validates if maturity date is of type str
            raise TypeError('maturity date should be string')

        if type(exercise_price) != 'int' or 'float':
            # Validates if exercise price is of type integer or float
            raise TypeError('exercise_prise must be integer or float')

        if type(optionType) != 'str':
            # Validates if option type is of type string
            raise TypeError('optionType must be string')

        #Assigning all parameters
        self.stock = stock
        self.maturity_date = maturity_date
        self.exercise_price = exercise_price
        self.optionType = optionType
        self.volatility = volatility
        self.altEstimation = self.getAltEstimation()

    def getAltEstimation(self):
        #todo: Query for yfinance's estimate
        estimation = self.stock.recommendations
        return estimation
