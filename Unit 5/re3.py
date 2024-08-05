import sys; args = sys.argv[1:]
idx = int(args[0])-50


#checked all in colorama before turning in ai grader
myRegexLst = [
  r"/(\w)+\w*\1\w*/i",
  r"/(\w)+(\w*\1){3}\w*/i",
  r"/^([10])[10]*\1$|^[10]$/",
  r"/\b(?=\w*cat)\w{6}\b/i",
  r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i",
  r"/\b(?!\w*cat)\w{6}\b/i",
  r'/\b((\w)(?!\w*\2))+\b/i',
  r"/^(1(?!0011)|0)*$/",
  r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
  r"/^(?!.*1.1)[01]*$/",


  ...]

#tested on colorama

if idx < len(myRegexLst):
  print(myRegexLst[idx])

#Anirudh Mantha,1,2024