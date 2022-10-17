class Option:
    # @requires
    def __init__(self, maturity_date, exercise_price) -> None:
        #Validates if maturity date is of type str
        if type(maturity_date) != 'str':
            raise TypeError('maturity date should be string')

        self.maturity_date = maturity_date
        self.exercise_price = exercise_price