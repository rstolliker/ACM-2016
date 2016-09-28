#!/bin/python3

import sys
from collections import defaultdict
from itertools import combinations

s_len = int(input().strip())
s = input().strip()


occurrences = defaultdict(lambda: [""] * s_len)

for i, char in enumerate(s):
    occurrences[char][i] = char
    

resultlen = 0
for charlist1, charlist2 in combinations(occurrences.values(), 2):
    #print(charlist1, charlist2)
    result = 0
    lastchar = ""
    for letter1, letter2 in zip(charlist1, charlist2):
        current = letter1 or letter2
        #print(current, lastchar)
        if current:
            if current == lastchar:
                result = 0
                break
            else:
                lastchar = current
                result += 1
    resultlen = max(resultlen, result)

print(resultlen)
