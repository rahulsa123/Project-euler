import requests
import pprint
url = "https://projecteuler.net/project/resources/p098_words.txt"
data = str(requests.get(url).content)[2:-1]

data = list(map(lambda x: x[1: -1], data.split(",")))

words = {}
for i in data:
    words.setdefault(len(i), []).append(i)

# now remove all non anagram words

for word_len in words:
    ref = words[word_len].copy()
    words[word_len] = {}
    for word in ref:
        words[word_len].setdefault(frozenset(word), []).append(word)
    temp = []
    for set_frozen in words[word_len]:
        if len(words[word_len][set_frozen]) == 1:
            temp.append(set_frozen)
    for remove_set in temp:
        words[word_len].pop(remove_set)

for word_len in sorted(words.keys(), reverse=True):
    if len(words[word_len]) < 1:
        continue
    for r in range(int(10**(word_len*0.5-1))+1, int(10**(word_len**0.5))):


