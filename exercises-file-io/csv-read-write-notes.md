
Congratulations!
You've completed the scenario!

 
Back to All Scenarios
Python Cookbook: Data Encoding & Processing
Step 1 of 5
Reading and Writing CSV Data
Problem

You want to read or write data encoded as a CSV file.
Solution

For most kinds of CSV data, use the csv library. For example, suppose you have some stock market data in a file named stocks.csv like this:

    Symbol,Price,Date,Time,Change,Volume
    "AA",39.48,"6/11/2007","9:36am",-0.18,181800
    "AIG",71.38,"6/11/2007","9:36am",-0.15,195500
    "AXP",62.58,"6/11/2007","9:36am",-0.46,935000
    "BA",98.31,"6/11/2007","9:36am",+0.12,104800
    "C",53.08,"6/11/2007","9:36am",-0.25,360900
    "CAT",78.29,"6/11/2007","9:36am",-0.23,225400

Here’s how you would read the data as a sequence of tuples:

import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Process row
        ...

In the preceding code, row will be a tuple. Thus, to access certain fields, you will need to use indexing, such as row[0] (Symbol) and row[4] (Change).

Since such indexing can often be confusing, this is one place where you might want to consider the use of named tuples. For example:

from collections import namedtuple
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        # Process row
        ...

This would allow you to use the column headers such as row.Symbol and row.Change instead of indices. It should be noted that this only works if the column headers are valid Python identifiers. If not, you might have to massage the initial headings (e.g., replacing nonidentifier characters with underscores or similar).

Another alternative is to read the data as a sequence of dictionaries instead. To do that, use this code:

import csv
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        ...

In this version, you would access the elements of each row using the row headers. For example, row['Symbol'] or row['Change'].

To write CSV data, you also use the csv module but create a writer object. For example:

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]

with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

If you have the data as a sequence of dictionaries, do this:

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
    ]

with open('stocks.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

Discussion

You should almost always prefer the use of the csv module over manually trying to split and parse CSV data yourself. For instance, you might be inclined to just write some code like this:

with open('stocks.csv') as f:
    for line in f:
        row = line.split(',')
        # process row
        ...

The problem with this approach is that you’ll still need to deal with some nasty details. For example, if any of the fields are surrounded by quotes, you’ll have to strip the quotes. In addition, if a quoted field happens to contain a comma, the code will break by producing a row with the wrong size.

By default, the csv library is programmed to understand CSV encoding rules used by Microsoft Excel. This is probably the most common variant, and will likely give you the best compatibility. However, if you consult the documentation for csv, you’ll see a few ways to tweak the encoding to different formats (e.g., changing the separator character, etc.). For example, if you want to read tab-delimited data instead, use this:

# Example of reading tab-separated values
with open('stock.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        # Process row
        ...

If you’re reading CSV data and converting it into named tuples, you need to be a little careful with validating column headers. For example, a CSV file could have a header line containing nonvalid identifier characters like this:

Street Address,Num-Premises,Latitude,Longitude 5412 N CLARK,10,41.980262,-87.668452

This will actually cause the creation of a namedtuple to fail with a ValueError exception. To work around this, you might have to scrub the headers first. For instance, carrying a regex substitution on nonvalid identifier characters like this:

import re
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        # Process row
        ...

It’s also important to emphasize that csv does not try to interpret the data or convert it to a type other than a string. If such conversions are important, that is something you’ll need to do yourself. Here is one example of performing extra type conversions on CSV data:

col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        ...

Alternatively, here is an example of converting selected fields of dictionaries:

print('Reading as dicts with type conversion')
field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]

with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)

In general, you’ll probably want to be a bit careful with such conversions, though. In the real world, it’s common for CSV files to have missing values, corrupted data, and other issues that would break type conversions. So, unless your data is guaranteed to be error free, that’s something you’ll need to consider (you might need to add suitable exception handling).

Finally, if your goal in reading CSV data is to perform data analysis and statistics, you might want to look at the Pandas package. Pandas includes a convenient pandas.read_csv() function that will load CSV data into a DataFrame object. From there, you can generate various summary statistics, filter the data, and perform other kinds of high-level operations.
Terminal
Powered By Katacoda
