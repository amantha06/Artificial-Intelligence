import sys
import re

file_imp = sys.argv[1]
line = ""

with open(file_imp) as f:
    for i in f: line += '\n' + i.lower() + '\n'

# challenge 1

output = ""
compiled = []
minimum_list = []
min_len = 999999999999999999999999
reg_exp = re.compile(r"\b(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w+\b")

for i in reg_exp.finditer(line):
    st, f = i.span()
    for i in range(st, f): output += line[i]
    if len(output) < min_len: min_len = len(output)
    compiled.append(output)
    output = ""
for output in compiled:
    if len(output) == min_len: minimum_list.append(output)
print("#1", reg_exp, '\n', len(minimum_list), "total matches")
for output in minimum_list[0:5]: print(output)

print('\n')

# challenge 2
output = ""
compiled = []
minimum_list = []
min_len = 0
reg_exp = re.compile(
    r"\b[^aeiou \n]*[aeiou][^aeiou \n]*[aeiou][^aeiou \n]*[aeiou][^aeiou \n]*[aeiou][^aeiou \n]*[aeiou][^aeiou \n]*\b")

for i in reg_exp.finditer(line):
    st, f = i.span()
    for i in range(st, f): output += line[i]
    if len(output) > min_len: min_len = len(output)
    compiled.append(output)
    output = ""
for output in compiled:
    if len(output) == min_len: minimum_list.append(output)
print("#2", reg_exp, '\n', len(minimum_list), "total matches")
for output in minimum_list[0:5]: print(output)

# challenge 3
output = ""
compiled = []
minimum_list = []
min_len = 0
reg_exp = re.compile(r"\b(\w)(?!\w*\1+\w*\1\b)\w*\1\b")

for i in reg_exp.finditer(line):
    st, f = i.span()
    for i in range(st, f): output += line[i]
    if len(output) > min_len: min_len = len(output)
    compiled.append(output)
    output = ""
for output in compiled:
    if len(output) == min_len: minimum_list.append(output)
print("#2", reg_exp, '\n', len(minimum_list), "total matches")
for output in minimum_list[0:5]: print(output)

# challenge 4
output = ""
compiled = []
reg_exp = re.compile(r"\b(\w)\w\1\b|\b(\w)(\w)\w?\3\2\b|\b(\w)(\w)(\w)\w*\6\5\4\b")

for i in reg_exp.finditer(line):
    st, f = i.span()
    for i in range(st, f): output += line[i]
    compiled.append(output)
    output = ""
print("#4", reg_exp, '\n', len(compiled), "total matches")
for output in compiled[0:5]: print(output)

# challenge 5
output = ""
compiled = []
reg_exp = re.compile(
    r"\b(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)(?=\w*tb)(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)\w*\b|\b(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)(?=\w*bt)(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)\w*\b|\b(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)(?=\w*tb)(?!\w*t\w+b\w*)(?!\w*t\w+b\w*)\w*\b|\b(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)(?=\w*bt)(?!\w*t\w+b\w*)(?!\w*t\w+b\w*)\w*\b")

for i in reg_exp.finditer(line):
    st, f = i.span()
    for i in range(st, f): output += line[i]
    compiled.append(output)
    output = ""
print("#5", reg_exp, '\n', len(compiled), "total matches")
for output in compiled[0:5]: print(output)

# challenge 6
output = ""
compiled = []
min_len = 0
minimum_list = []
max_word_list = []
regex_list = []
reg_exp = re.compile(r"(\w)\1+")

for i in reg_exp.finditer(line):
    st, f = i.span()
    for i in range(st, f): output += line[i]
    if len(output) > min_len: min_len = len(output)
    compiled.append(output)
    output = ""
for output in compiled:
    if len(output) == min_len: minimum_list.append(output)
for output in minimum_list:
    modified = '\\b.*' + output + '.*\\b'
    regexex = re.compile(modified)
    regex_list.append(regexex)
    for i in regexex.finditer(line):
        worded = ""
        st, f = i.span()
        for j in range(st, f): worded += line[j]
        max_word_list.append(worded)

print("#6", reg_exp)
# for i in regex_list: print(i)
print(len(minimum_list), "total matches")
for output in max_word_list[0:5]: print(output)

# challenge 7
# starting here it gets really weird, the regEx that I decided to do was periodic
# there are many instances, where it goes from 1, 2, 3, 4 ....
#so there are technically name reg ex, but as seen in line 141 it updates every time in the loop

output = ""
compiled = []
max_list = []
counter = 1
terminator = True

while terminator == True:
    terminator = False
    regexex_store = "(\w)+(\w*\\1\w*){" + str(counter) + ",}"
    reg_exp = re.compile(regexex_store)
    for i in reg_exp.finditer(line):
        terminator = True
        st, f = i.span()
        for j in range(st, f): output += line[j]
        compiled.append((counter, output))
        output = ""
    counter += 1
for i, j in compiled:
    if i == counter - 2: max_list.append(j)

print("#7", "re.compile('(\\w)+(\\w*\\1\\w*){" + str(1) + ",}')")
print(len(max_list), "total matches")
for output in max_list[0:5]: print(output)

# challenge 8
#same situation as 7

output = ""
compiled = []
max_list = []
counter = 1
terminator = True

while terminator == True:
    terminator = False
    regexex_store = "\\b\w*(\w\w)+(\w*\\1\w*){" + str(counter) + ",}\\b"
    reg_exp = re.compile(regexex_store)
    for i in reg_exp.finditer(line):
        terminator = True
        st, f = i.span()
        for j in range(st, f): output += line[j]
        compiled.append((counter, output))
        output = ""
    counter += 1
for i, j in compiled:
    if i == counter - 2: max_list.append(j)

print("#8", "re.compile('\\b\w*(\w\w)+(\w*\\1\w*){" + str(1) + ",}\\b')")
print(len(max_list), "total matches")
for output in max_list[0:5]: print(output)

# challenge 9
#same situation as 7

output = ""
compiled = []
max_list = []
counter = 1
terminator = True

while terminator == True:
    terminator = False
    regexex_store = "\\b([aeiou]*[^ \\naeiou][aeiou]*){" + str(counter) + ",}\\b"
    reg_exp = re.compile(regexex_store)
    for i in reg_exp.finditer(line):
        terminator = True
        st, f = i.span()
        for j in range(st, f): output += line[j]
        compiled.append((counter, output))
        output = ""
    counter += 1
for i, j in compiled:
    if i == counter - 2: max_list.append(j)

print("#9", "re.compile('\\b([aeiou]*[^ \\naeiou][aeiou]*){" + str(1) + ",}\\b')")
print(len(max_list), "total matches")
for output in max_list[0:5]: print(output)

# challenge 10

output = ""
compiled = []
max_list = []
passed_limit = set()
maxnum_tresh = 0
reg_exp = re.compile(r"(\w)+(\w*\1\w*){2,}")

for i in reg_exp.finditer(line):
    st, f = i.span()
    for i in range(st, f): output += line[i]
    passed_limit.add(output)
    output = ""
for output in line.split():
    if not output in passed_limit:
        compiled.append(output)
        if len(output) > maxnum_tresh: maxnum_tresh = len(output)
for i in compiled:
    if len(i) == maxnum_tresh: max_list.append(i)

print("#10", reg_exp)
print(len(max_list), "total matches")
for i in max_list[0:5]: print(i)
