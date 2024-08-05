import sys; args = sys.argv[1:]
idx = int(args[0])-40


#checked all in colorama
myRegexLst = [
  r"/^[.xo]{64}$/i",
  r"/^[xo]*\.[ox]*$/i",
  r"/^(x+o*)?\.|\.(o*x+)?$/i",
  r"/^.(..)*$/s",
  r"/^(0|1[10])([01]{2})*$/",
  r"/\w*(a[ieuo]|e[uiao]|i[uaeo]|o[aeui]|u[aeoi])\w*/i",
  r"/^(1?0+?)*1*$/",
  r"/^\b[cb]*a?[bc]*$/",
  r"/^(a[bc]*a|[cb])+$/",
  r"/^((2|1[02]*1)[02]*)+$/",

...]

#tested on colorama
if idx < len(myRegexLst):
  print(myRegexLst[idx])

#Anirudh Mantha,1,2024