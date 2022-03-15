import csv

high_wages = []
desired_wage = 40000

with open('data/wages.csv', 'r') as infile:
    reader = csv.reader(infile)
    # header = next(reader)  # capture header line.
    next(reader)  # Skip the header line.

    print('reader: ')
    for row in reader:
        annual_wage = int(row[2])  # (A)
        if annual_wage >= desired_wage:
            print(high_wages)
            high_wages.append(row)

with open('data/high-wages.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    print('writer: ')
    # writer.writerow(header) # write header row
    for row in high_wages:
        writer.writerow(row)
    print(high_wages)

# outputs without headers
