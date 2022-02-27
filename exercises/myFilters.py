import csv
# import collections

# with open('data/neos.csv', 'r') as f:
# 	reader = csv.DictReader(f)
# 	count = 0
# 	for row in reader:
# 		count +=1
# print(count)

filterOutNames = ''

with open('data/neos.csv', 'r') as f:
	reader = csv.DictReader(f)
	count = 0
	for row in reader:
		if row['name'] != filterOutNames:
			count +=1
			# print(row['name'])

print(count)

# with open('data/neos.csv', 'r') as f:
# 	reader = csv.DictReader(f)
# 	# c = collections.Counter()
# 	# reader(c)
# 	for row in reader:
# 		c = collections.Counter(row)
# print(c)