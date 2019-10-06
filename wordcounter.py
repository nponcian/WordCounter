#!/usr/bin/python3

from collections import defaultdict

DIR_PATH = "./FilesToProcess/"
INPUT_FILE = DIR_PATH + "Input.txt"
WORDS_SEPARATORS_FILE = DIR_PATH + "WordsSeparators.txt"
WORDS_TO_COUNT_FILE = DIR_PATH + "WordsToCount.txt"
WORDS_TO_IGNORE_FILE = DIR_PATH + "WordsToIgnore.txt"

with open(INPUT_FILE) as fileInput:
    inputLines = fileInput.readlines()
with open(WORDS_SEPARATORS_FILE) as fileWordsSeparators:
    wordsSeparators = fileWordsSeparators.read()
with open(WORDS_TO_COUNT_FILE) as fileWordsToCount:
    wordsToCount = list(filter(None, fileWordsToCount.read().split("\n")))
with open(WORDS_TO_IGNORE_FILE) as fileWordsToIgnore:
    wordsToIgnore = list(filter(None, fileWordsToIgnore.read().split("\n")))

wordDict = defaultdict(int)
SPACE = " "

for line in inputLines:
    for separator in wordsSeparators:
        line = line.replace(separator, SPACE)

    for currentWord in line.split():
        currentWordLower = currentWord.casefold()
        if currentWordLower not in wordsToIgnore and\
            (len(wordsToCount) == 0 or currentWordLower in wordsToCount):
            wordDict[currentWordLower] += 1

print("\n".join(\
        [" : ".join(map(str, item)) for item in sorted(\
            wordDict.items(), key = lambda x : x[1], reverse = True)]))
