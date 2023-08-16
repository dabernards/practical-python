# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    '''
    Parse a CSV file into a list of records (provided version)
    '''

    if select and not has_headers:
        raise RuntimeError("passing 'select' argument requires headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
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
