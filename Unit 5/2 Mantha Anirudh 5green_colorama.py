import re
import sys
from colorama import init, Back, Fore
s = "While inside they wined and dined, safe from the howling wind.\nAnd she whined, it seemed, for the 100th time, into the ear of her friend,\nWhy indeed should I wind the clocks up, if they all run down in the end?"

init()

regular_exp = sys.argv[1]
modified = regular_exp[1:]
flags = ""
if modified.index("/") != len(modified):
    enders = modified[modified.index("/") + 1:]
    modified = modified[:modified.index("/")]



if len(enders) == 0: store_value = re.compile(modified)
elif len(enders) == 1:
    if enders == 'i': store_value = re.compile(modified, re.I)
    elif enders == 'm': store_value = re.compile(modified, re.M)
    elif enders == 's': store_value = re.compile(modified, re.S)
elif len(enders) == 2:
    if enders == 'im' or enders == 'mi': store_value = re.compile(modified, re.I | re.M)
    elif enders == 'is' or enders == 'si': store_value = re.compile(modified, re.I | re.S)
    if enders == 'sm' or enders == 'ms': store_value = re.compile(modified, re.S | re.M)
elif len(enders) == 3: store_value = re.compile(modified, re.S | re.M | re.I)


highlight = ""
index = []
starting = []
color = Back.YELLOW
for i in store_value.finditer(s):
    st, f = i.span()
    starting.append((st, f))
    for j in range(st, f): index.append(j)
    index.append("x")

terminator = False
for i in range(len(s)):
    if not i in index: highlight += s[i]
    else:
        if terminator == True:
            color = Back.CYAN
            highlight += color + s[i] + Back.RESET
            if index[index.index(i) + 1] == "x":
                terminator = False
                color = Back.YELLOW
        elif index[index.index(i) + 1] == "x" and index.index(i) + 1 != len(index) - 1:
            highlight += color + s[i] + Back.RESET
            if index[index.index(i) + 2] == i + 1: terminator = True
        else: highlight += color + s[i] + Back.RESET

print(highlight)

#changed from the function i used earlier, because i was not able to understand what it did.