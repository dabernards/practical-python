


with open('Data/portfolio.csv', 'rt') as f:
    # data = f.read()
    headers = next(f)
    # headers = f.readline()
    for line in f:
        print(line.strip().split(','))
# print(data)