# fileparse.py
#
# Exercise 3.3
import csv

# def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
def parse_csv(data, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    '''
    Parse a CSV file into a list of records (provided version)
    '''
    if type(data) is str:
        raise TypeError('Looks like data is a string not a data array')
    rows = csv.reader(data, delimiter=delimiter)

    if select and not has_headers:
        raise RuntimeError("passing 'select' argument requires headers")

    if has_headers:
        headers = next(rows)

    # with open(filename) as f:
    #     rows = csv.reader(f, delimiter=delimiter)

    # Read the file headers
    records = []
    for i, row in enumerate(rows):
        if not row:    # Skip rows with no data
            continue
        try:
            if select:
                # make sure select is in the right order
                row = [item for item,head in zip(row, headers) if head in select]
                headers = [head for head in headers if head in select]
            if types:
                row = [func(item) for item, func in zip(row, types)]

            if has_headers:
                record = {head: item for item, head in zip(row, headers)}
            else:
                record = tuple(row)
            records.append(record)
        except Exception as e:
            if not silence_errors:
                print(f"Row {i+1:d}: Couldn't convert {row}")
                print(f"Row {i+1:d}: Reason {e}")

    return records
