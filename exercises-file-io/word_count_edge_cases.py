# Count words
import collections

with open("data/hamlet.txt", "r") as f:
    data = f.read()
replaceNewline = data.replace("\n", " ")
words = replaceNewline.split(" ")
c = collections.Counter(words)

tenMostCommon = c.most_common(10)
for i in tenMostCommon:
    print(i[0], i[1])

print("word count", sum(c.values()))
