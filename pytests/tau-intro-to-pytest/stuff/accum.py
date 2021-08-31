# class that saves tally of numbers
class Accumulator:

    def __init__(self):
        self._count = 0

    @property            #properties control how callers can "get" and "set" values. With this property, a caller can get the value of count but cannot set the value directly with an assignment statement.
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more