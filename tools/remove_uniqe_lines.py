import time as t
import sys

def get_time():
    """This Function returns the current hour, minute and second in a human readable format."""
    return t.strftime('%H:%M:%S')

try:
    fileName = input("Input filename: ")
except FileNotFoundError:
    print('You didn\'t supply a valid filename.')
    sys.exit(1)

with open(fileName, 'r', encoding="utf-8") as f:
    file = f.readlines()

wordList = []
badList = []

for line in file:
    if line in wordList:
        badList.append(line)
    else:
        wordList.append(line)

file = open(fileName, 'w', encoding="utf-8")

for line in wordList:
    file.write(line)

file.close()

print(f'[{get_time()}]: {len(badList)} duplicate lines removed from {fileName}.')
