# report.py
#
# Exercise 2.4

from fileparse import parse_csv
# import csv

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

    # portfolio = []
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for row in rows:
    #         holding = dict(zip(headers, row))
    #         # holding = (row[0], int(row[1]), float(row[2]))
    #         stock = {
    #             'name': holding['name'], 
    #             'shares': int(holding['shares']), 
    #             'price': float(holding['price'])
    #         }
    #         portfolio.append(stock)
    portfolio = parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True)

    return portfolio

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
    # prices = {}
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     for row in rows:
    #         if row != []:
    #             prices[row[0]] = float(row[1])
    prices = parse_csv(filename, types=[str,float], has_headers=False)
    return dict(prices)

def make_report(portfolio, prices):
    ''' Generate a report string '''
    report =[]
    for item in portfolio:
        report.append((item['name'], item['shares'], prices[item['name']], item['price']-prices[item['name']]))
    return report

def print_report(report):
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


# print(read_portfolio('Data/portfolio.csv'))
# print(read_portfolio_dict('Data/portfolio.csv'))
# print(read_prices('Data/prices.csv'))

# portfolio = read_portfolio('Data/portfolio.csv')


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

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print(f'{portfolio_filename:-^43s}')
    print_report(report)
    return

# portfolio_report('Data/portfoliodate.csv', 'Data/prices.csv')
portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
