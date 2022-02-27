# solution
import collections

def count_unique_words(filename):
    words = collections.Counter()
    with open(filename, "r") as f:  # f is a stream?
        for line in f:
            words.update(line.split())

    for word, count in words.most_common(10):
        print(word, count)

filename = "data/hamlet.txt"
count_unique_words(filename)
