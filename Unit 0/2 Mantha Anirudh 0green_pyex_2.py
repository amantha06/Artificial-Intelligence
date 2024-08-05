import sys

#s = sys.argv[1]
s = "abcde edcba"
print(s[2]) ###1
print(s[4]) ###2
print(len(s)+1) ###3
print(s[0]) ###4
print(s[-1]) ###5
print(s[-2]) ###6
print(s[3:7])###7
print(s[-5:])###8
print(s[2:])###9
print(s[::2])###10
print(s[1::3])###11
print(s[::-1])###12
print(s.find(' '))###13
print(s[:-1])###14
print(s[1:])###15
print(s.lower())###16
print(s.split(" "))###17
print(len(s.split(" ")))###18
print(list(s.strip(" ")))###19
print(''.join(sorted(s)))###20
print(s.split(" ", 1)[0])###21
print((s == s[::-1]))###22









