# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=False):
    '''
    Parse a CSV file into a list of records (provided version)
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        if has_headers:
            headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
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
    return records
