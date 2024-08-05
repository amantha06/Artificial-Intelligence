import sys; args = sys.argv[1:]
idx = int(args[0])-60

myRegexLst = [
  r"/^((?!010)\d)*$/",
  r"/^((?!101)(?!010)\d)*$/",
  r"/^([01])([01]*\1)?$/",
  r"/(\b((\w)(?!\w*\3\b))+\b)/i",
  r"/\w*((\w)(?=\w*\2))\w*((\1\w*){3}|(?!\2)(\w)(?=\w*\5)\w*)\b/i",
  r"/\b(?=(\w)+(\w*\1){2})((\w)(?!\w*\4)|\1)+\b/im",
  r"/\b([^aeiou\s]*([aeiou])(?!\w*\2)){5}\w*?\b/i",
  r"/^(?=^(0*(10*1)?)*$)[01]([01]{2})*$/",
  r"/^(0$|1(01*0)*10*)+$/",
  r"/^1(10*1|01*0)*(01*)?$/",
]

''

#tested on colorama file

if idx < len(myRegexLst):
  print(myRegexLst[idx])
#Anirudh Mantha, 1, 2024




