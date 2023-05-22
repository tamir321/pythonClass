class Date(object):
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"the date is -- {self.day} / {self.month} / {self.year}"
    """
       The classmethod decorator decorates methods as static methods, like staticmethod. 
       Not like staticmethod, the classmethod receives the class object as the first parameter
    """

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(lambda val: int(val), date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    """
         The staticmethod decorator modifies a method so that it does not use the self variable.
         Static method do not have access to any attribute of a specific instance of the class.
    """
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(lambda val: int(val), date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


print(Date.is_date_valid("1-1-1987"))

new_date = Date.from_string("1-1-1987")
print(new_date)
