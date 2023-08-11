# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None):
    '''
    Parse a CSV file into a list of records (provided version)
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        if select is None:
            select = headers
        if types is None:
            types = [str for _ in headers]
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = {x:z(y) for x,y,z in zip(headers, row, types) if x in select}
            records.append(record)

    return records
