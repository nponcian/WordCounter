#!/usr/bin/python3

from collections import defaultdict

DIR_PATH = "./FilesToProcess/"
WORDS_SEPARATORS_FILE = "WordsSeparators.txt"
WORDS_TO_COUNT_FILE = "WordsToCount.txt"
WORDS_TO_IGNORE_FILE = "WordsToIgnore.txt"

with open(DIR_PATH + WORDS_SEPARATORS_FILE) as fileWordsSeparators:
    wordsSeparators = fileWordsSeparators.read()
with open(DIR_PATH + WORDS_TO_COUNT_FILE) as fileWordsToCount:
    wordsToCount = fileWordsToCount.readlines()
with open(DIR_PATH + WORDS_TO_IGNORE_FILE) as fileWordsToIgnore:
    wordsToIgnore = fileWordsToIgnore.read().split("\n")

wordDict = defaultdict(int)
SPACE = " "

for line in wordsToCount:
    for separator in wordsSeparators:
        line = line.replace(separator, SPACE)

    for currentWord in line.split():
        currentWordLower = currentWord.casefold()
        if currentWordLower not in wordsToIgnore:
            wordDict[currentWordLower] += 1

print("\n".join(\
        [" : ".join(map(str, item)) for item in sorted(\
            wordDict.items(), key = lambda x : x[1], reverse = True)]))
