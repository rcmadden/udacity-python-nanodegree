import csv
import json
import collections

print('Enter Relative File Path:')
# filePath = input()
filePath = 'data/hamlet.txt'
# TODO: filepath strip to current folder and file only

words = collections.Counter()

with open(filePath, 'r') as f:
	if filePath.lower().endswith('.txt'):
		contents = f.read()
		# lines = len(contents)

		lines = 0
		for char in contents:
			if char == '\n':
				lines +=1
		#add 1 if last '\n' is not last char of file
		#lines +=1

with open(filePath, 'r') as file:

    wordcount = 0
    for line in file:
        words.update(line.split())

    for word in words:
        wordcount += words[word]

spaces = '    '
print(f'{filePath} file:')
print(f'{spaces}type: ', type(contents))
print(f'{spaces}length: ', len(contents))
print(f'{spaces}word count:', wordcount)
print(f'{spaces}lines: ', lines)

# inputFieldName = input()
# blank = ''

# with open('data/neos.csv', 'r') as f:
# 	print(type(f))
# 	print(f)
# 	reader = csv.DictReader(f)
# 	print(type(reader))
# 	print(reader)

# 	count = 0
# 	for row in reader:
# 		if row[inputFieldName] != blank:
# 			count +=1
# 			# print(row['name'])

# print(count, "have a", inputFieldName)

# TODO: take either json or csv
# Create a file reader data summarizer

# dict_keys(['signature', 'count', 'fields', 'data'])
# fields == ['des', 'orbit_id', 'jd', 'cd', 'dist', 'dist_min', 'dist_max', 'v_rel', 'v_inf', 't_sigma_f', 'h']
# data == list of lists  ['2010 XB24', '19', '2488069.369087819', '2099-Dec-31 20:51', '0.126306889299689', '0.125428658725108', '0.127185695415594', '16.6758717193855', '16.6746066532063', '01:03', '21.8']
# with open('data/cad.json', 'r') as f:
	# data = json.load(f)
	
# print(len(data['data']))
