# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).strip().split(',')
    data = f.read().strip()
cost = 0

for item in data.split('\n'):
    _, shares, price = item.split(',')
    cost += int(shares)*float(price)

print(f'Total cost {cost}')

# import gzip
# with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
#     for line in f:
#         print(line, end="")