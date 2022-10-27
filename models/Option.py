import string
import datetime
from enum import Enum

class Option:
    def __init__(self, maturity_date, exercise_price, optionType, stock) -> None:
        """
        Class for a stock option
        @requires optionType to be either 'call' or 'put'
        @param maturity_date: gives the date of maturity
        @param exercise_price: gives the price for which the price is bought
        @param optionType: gives the type of option
        """

        class Optiontype(Enum):
            CALL = 1
            PUT = 2

        if type(maturity_date) != 'str':
            # Validates if maturity date is of type str
            raise TypeError('maturity date should be string')

        if type(exercise_price) != 'int' or 'float':
            # Validates if exercise price is of type integer or float
            raise TypeError('exercise_prise must be integer or float')

        if type(optionType) != 'str':
            # Validates if option type is of type string
            raise TypeError('optionType must be string')

        self.stock = stock;
        self.maturity_date = maturity_date
        self.exercise_price = exercise_price

        if string.lower(optionType) == 'call':
            self.optionType = Optiontype.CALL
        elif string.optionType == 'put':
            self.optionType = Optiontype.PUT
        else:
            raise AttributeError('Optiontype must be either call or put')