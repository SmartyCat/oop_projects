class Month:
    def __init__(self, year, month):

        self.year = year
        self.month = month

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __repr__(self):
        return f"Month({self.year},{self.month})"

    def __eq__(self, value):
        if isinstance(value, Month):
            return self.year == value.year and self.month == value.month
        elif isinstance(value, tuple) and len(value) == 2:
            return self.year == value[0] and self.month == value[1]
        return NotImplemented

    def __lt__(self, value):
        if isinstance(value, Month):
            if self.year == value.year:
                return self.month < value.month
            return self.year < value.year
        elif isinstance(value, tuple) and len(value) == 2:
            if self.year == value[0]:
                return self.month < value[1]
            return self.year == value[0]

    def __le__(self, value):
        if isinstance(value, Month):
            if self.year == value.year:
                return self.month <= value.month
            return self.year <= value.year
        elif isinstance(value, tuple) and len(value) == 2:
            if self.year == value[0]:
                return self.month <= value[1]
            return self.year <= value[0]



