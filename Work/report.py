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
    portfolio = parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True)

    return portfolio

def read_prices(filename):
    ''' reads a set of prices from csv file and generates dictionary '''
    prices = parse_csv(filename, types=[str,float], has_headers=False)
    return dict(prices)

def make_report(portfolio, prices):
    ''' Generate a report string '''
    report =[]
    for item in portfolio:
        report.append((item['name'], item['shares'], prices[item['name']], prices[item['name']]-item['price']))
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



def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print(f'{portfolio_filename:-^43s}')
    print_report(report)
    return

# portfolio_report('Data/portfoliodate.csv', 'Data/prices.csv')
portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
