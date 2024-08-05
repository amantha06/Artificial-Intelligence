
import sys



def main(list):

    if(list[1] == "A"):
        return int(list[2]) + int(list[3]) + int(list[4])
    if(list[1] == "B"):
        returnvalue = 0
        for index, value in enumerate(list):
            if(value.isnumeric()):
                returnvalue += int(value)
        return returnvalue

    if(list[1] == "C"):
        returnlist = [value for index, value in enumerate(list) if (value.isnumeric()) if int(value) % 3 == 0]
        return returnlist
    if(list[1] == "D"):
        return [fib(n) for n in range((int)(list[2]))]

    if(list[1] == "E"):
        minbound, maxbound = (int)(list[2]), (int)(list[3])
        returnlist = [(minbound + n)*(minbound + n) - 3*(minbound + n) + 2 for n in range(maxbound-(minbound-1))]
        return returnlist

    if(list[1] == "F"):
        sidea, sideb, sidec = (float)(list[2]), (float)(list[3]), (float)(list[4])
        if sidea + sideb > sidec and sidea + sidec > sideb and sideb + sidec > sidea:
            peri = (sidea + sideb + sidec)/2
            return pow((peri*(peri-sidea)*(peri-sideb)*(peri-sidec)), 0.5)
    if(list[1] == "G"):
        returnlist = []
        strval = (str)(list[2])
        inta, inte, inti, into, intu = strval.count("a"), strval.count("e"), strval.count("i"), strval.count("o"), strval.count("u")
        return "a: " + (str)(inta) + " e: " + (str)(inte)+ " i: " + (str)(inti)+ " o: " + (str)(into)+ " u: "  + (str)(intu)

def fib(inpnumiter):
    if inpnumiter == 0 or inpnumiter == 1:
        return 1
    else:
        return fib(inpnumiter-1) + fib(inpnumiter-2)




