# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records (provided version)
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        if select is None:
            select = headers
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = {x:y for x,y in zip(headers, row) if x in select}
            records.append(record)

    return records
