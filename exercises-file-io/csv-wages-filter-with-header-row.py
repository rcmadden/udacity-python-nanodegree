import csv

desired_wage = 40000
high_wages = []
with open('data/wages.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    print('reader: ')
    for elem in reader:
        print(elem)  # <= Each of these elements are `dict`s, not `list`s
        if int(elem['annual_wage']) >= desired_wage:
            high_wages.append(elem)

with open('data/high-wages-with-header.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=high_wages[0].keys())
    print('writer: ')
    writer.writeheader()
    for elem in high_wages:
        print(elem)
        writer.writerow(elem)  # passing a dict to writerow.
