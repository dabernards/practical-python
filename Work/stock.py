

class Stock:
    ''' wrapper for stock holdings '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        ''' calc cost of a stock holding '''
        return self.shares * self.price

    def sell(self, sale):
        ''' sell some shares of stock '''
        self.shares -= sale
        return self.shares
