import csv
from collections import namedtuple

# with open('data/neos_10.csv') as f:
#     f_csv = csv.reader(f)
#     fieldnamez = next(f_csv)
#     Rowz = namedtuple('Rowz', fieldnamez)
#     for r in f_csv:
#         rowz = Rowz(*r)
#         print(rowz)

from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row.Symbol, row)


