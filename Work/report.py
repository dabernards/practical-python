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
            holding = dict(zip(headers, row))
            # holding = (row[0], int(row[1]), float(row[2]))
            protfolio.append({'name': holding['name'], 'shares': int(holding['shares']), 'price': float(holding['price'])})
    return protfolio

# def read_portfolio_dict(filename):
#     ''' Read a portfolio csv file and returns data as a list of dictionaries '''

#     protfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             holding = {'stock': row[0], 'shares': int(row[1]), 'price': float(row[2])}
#             protfolio.append(holding)
#     return protfolio

def read_prices(filename):
    ''' reads a set of prices from csv file and generates dictionary '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row != []:
                prices[row[0]] = float(row[1])
    return prices

def make_report(portfolio, prices):
    ''' Generate a report string '''
    report =[]
    for item in portfolio:
        report.append((item['name'], item['shares'], prices[item['name']], item['price']-prices[item['name']]))
    return report

# print(read_portfolio('Data/portfolio.csv'))
# print(read_portfolio_dict('Data/portfolio.csv'))
# print(read_prices('Data/prices.csv'))

# portfolio = read_portfolio('Data/portfolio.csv')
portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name','Shares','Price','Change')
for header in headers:
    print(f'{header:>10s} ', end="")
print()
print(f'{"-"*10:10s} '*4)
for r in report:
    # print(r)
    # print('%10s %10d %10.2f %10.2f' % r)
    currency = f'${r[2]:.2f}'
    print(f'{r[0]:>10s} {r[1]:>10d} {currency:>10s} {r[3]:>10.2f}')    

# from collections import Counter
# total_shares = Counter()
# for item in portfolio:
#     total_shares[item['name']] += item['shares']

# print(total_shares['IBM'])

# from collections import defaultdict
# holdings=defaultdict(list)
# for item in portfolio:
#     holdings[item['name']].append((item['shares'], item['price']))
# print(holdings['IBM'])

