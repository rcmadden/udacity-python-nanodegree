import collections

words = collections.Counter()

with open('data/hamlet.txt', 'r') as file:
    for line in file:
        words.update(line.split())

for word, count in words.most_common(10):
    print(word, count)


