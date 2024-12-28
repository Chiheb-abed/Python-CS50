class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self.cookie_nbr = 0

    def __str__(self):
        if self.cookie_nbr==0 :
            return ""
        else:
            return "🍪" * self.cookie_nbr


    def deposit(self, n):
        if  (n + self.cookie_nbr <= self._capacity) and n > 0 :
            self.cookie_nbr += n
        else:
            raise ValueError

    def withdraw(self, n):
        if n <=  self.cookie_nbr and n > 0:
            self.cookie_nbr -=  n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self.cookie_nbr

