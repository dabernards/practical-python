# pcost.py
#
# Exercise 1.27

# Original Code
# with open('Data/portfolio.csv', 'rt') as f:
#     headers = next(f).strip().split(',')
#     data = f.read().strip()
# cost = 0

# for item in data.split('\n'):
#     _, shares, price = item.split(',')
#     cost += int(shares)*float(price)

# print(f'Total cost {cost}')

#Updated for functions
# def portfolio_cost(filename):
#     with open(filename, 'rt') as f:
#         headers = next(f).strip().split(',')
#         data = f.read().strip()
#     cost = 0

#     try:
#         for item in data.split('\n'):
#             stock_name, shares, price = item.split(',')
#             cost += int(shares)*float(price)
#     except ValueError:
#         print(f'invalid input for {stock_name}')

#     return cost

#Updated for csv module and cli
import sys
import csv
from report import read_portfolio

def portfolio_cost(filename):
    # with open(filename, 'rt') as f:
    #     data = csv.reader(f)
    #     header=next(data)
    #     cost = 0

    #     for i, item in enumerate(data, start=1):
    #         record = dict(zip(header, item))
    #         try:
    #             shares = int(record['shares'])
    #             price = float(record['price'])
    #             cost += int(shares)*float(price)
    #         except ValueError:
    #             print(f'Row {i}: Couldn\'t convert {item}')
    portfolio = read_portfolio(filename)
    cost = sum([item['shares']*item['price'] for item in portfolio])
    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)


# import gzip
# with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
#     for line in f:
#         print(line, end="")