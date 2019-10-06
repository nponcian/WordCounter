#!/usr/bin/python3

from collections import defaultdict

with open("WordsToCount.txt") as fileWordsToCount:
    wordsToCount = fileWordsToCount.readlines()
with open("WordsToIgnore.txt") as fileWordsToIgnore:
    wordsToIgnore = fileWordsToIgnore.read()

wordDict = defaultdict(int)
wordsToIgnore = wordsToIgnore.split("\n")

for line in wordsToCount:
    line = line.replace(",", " ")
    line = line.replace("/", " ")
    line = line.replace(":", " ")
    line = line.replace("(", " ")
    line = line.replace(")", " ")
    for split in line.split():
        if split.lower() in wordsToIgnore:
            continue

        wordDict[split.lower()] += 1

print("\n".join( \
        [" : ".join(map(str, item)) for item in sorted( \
            wordDict.items(), key = lambda x : x[1], reverse = True)]))
