# ticker.py

from follow import follow
import csv
import report
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    stocks = { item.name for item in portfolio }
    lines = follow(logfile)
    lines = parse_stock_data(lines)
    lines = filter_symbols(lines, stocks)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for line in lines:
        formatter.row([line['name'],f"{line['price']:0.2f}", f"{line['change']:0.2f}"])

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
