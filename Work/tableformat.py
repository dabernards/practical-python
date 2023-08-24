# tableformat.py
# provided class

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {fmt}')

def print_table(portfolio, select, formatter):
    ''' print arbitrary table '''
    formatter.headings(select)
    for s in portfolio:
        for item in [getattr(s,col) for col in select]:
            print(f'{str(item):>10s} ', end="")
        print()


class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print('<tr><th>','</th><th>'.join(headers),"</th></tr>", sep="")

    def row(self, rowdata):
        print('<tr><th>','</th><th>'.join(rowdata),"</th></tr>", sep="")


class FormatError(Exception):
    pass