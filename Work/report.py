# report.py
#
# Exercise 2.4

from fileparse import parse_csv
from stock import Stock
import tableformat

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
    with open(filename, 'rt') as f:
        portfolio = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True)
    portfolio = [Stock(item['name'], item['shares'], item['price']) for item in portfolio]
    return portfolio

def read_prices(filename):
    ''' reads a set of prices from csv file and generates dictionary '''
    with open(filename, 'rt') as f:
        prices = parse_csv(f, types=[str,float], has_headers=False)
    return dict(prices)

def make_report(portfolio, prices):
    ''' Generate a report string '''
    report =[]
    for item in portfolio:
        report.append((item.name, item.shares, prices[item.name], prices[item.name]-item.price))
    return report

def print_report(report, formatter):
    formatter.headings(['Name','Shares','Price','Change'])
    # for header in headers:
    #     print(f'{header:>10s} ', end="")
    # print()
    # print(f'{"-"*10:10s} '*4)
    for name, shares, price, change in report:
        # print(r)
        # print('%10s %10d %10.2f %10.2f' % r)
        # currency = f'${r[2]:.2f}'
        # print(f'{r[0]:>10s} {r[1]:>10d} {currency:>10s} {r[3]:>10.2f}')    
        rowdata = [name, str(shares), f'${price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print(f'{portfolio_filename:-^43s}')
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    return




# portfolio_report('Data/portfoliodate.csv', 'Data/prices.csv')

def main(args, fmt="txt"):
    ''' normal way to use report.py 
    if passed using sys.argv, first argument will be report.py!
    '''

    portfolio_report(args[1],args[2], fmt)


if __name__ == '__main__':
    import sys
    if len(sys.argv)==3:
        main(sys.argv)
    if len(sys.argv)==4:
        main(sys.argv[:-1], fmt=sys.argv[-1])


