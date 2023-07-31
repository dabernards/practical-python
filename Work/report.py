# report.py
#
# Exercise 2.4

import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost

def read_portfolio(filename):
    ''' Read a portfolio csv file and returns data as a list of tuples '''

    protfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            protfolio.append(holding)
    return protfolio

def read_portfolio_dict(filename):
    ''' Read a portfolio csv file and returns data as a list of dictionaries '''

    protfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            protfolio.append(holding)
    return protfolio

def read_prices(filename):
    ''' reads a set of prices from csv file and generates dictionary '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            if row != []:
                prices[row[0]] = float(row[1])
    return prices

# print(read_portfolio('Data/portfolio.csv'))
# print(read_portfolio_dict('Data/portfolio.csv'))
# print(read_prices('Data/prices.csv'))

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

for stock, shares, init_price in portfolio:
    if stock in prices:
        print(f'{stock:<4s}\t{init_price:0.2f}\t{prices[stock]:0.2f}\t{(prices[stock]-init_price)*shares: 0.2f}')
    else:
        print(f'Unknown price for stock {stock}')
# bit of an oddity here, that AA stock doesn't exist in the prices file