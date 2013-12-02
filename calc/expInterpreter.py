import operator
import re

operatorDict = {'+': operator.add, '-': operator.sub,
                '*': operator.mul, '/': operator.div,
                '%': operator.mod }
priOpe = ['*', '/', '%']

def findClosestBrace(mystr):
    a, b = -1,-1
    for i in range(len(mystr)):
        if mystr[i] == '(':
            a = i
        elif mystr[i] == ')':
            b = i
            if a >= 0: return a, b
    return -1, -1

def exp2list(expStr):
    li = map(lambda x: x.strip(),re.split("(\D+)", expStr.strip()))
    res = []
    for m in li:
        try:
            c = int(m)
        except:
            c = m
        finally:
            res.append(c)
    return res

def simplifyList(explist):
    length = len(explist)
    if any(map(lambda x: x in explist, priOpe)):
        for i in range(length):
            if any(map(lambda x: x == explist[i], priOpe)):
                res = operatorDict[explist[i]](explist[i-1], explist[i+1])
                return explist[:i-1] + [res] + explist[i+2:]
    else:
        i = 1
        res = operatorDict[explist[i]](explist[i-1], explist[i+1])
        return explist[:i-1] + [res] + explist[i+2:]

def evalexplist(explist):
    if len(explist) < 3: return explist[0]
    slist = simplifyList(explist)
#   print slist
    return evalexplist(slist)

def evalexp(expstr):
    return evalexplist(exp2list(expstr))

def evalwithBrackets(myexp):
    a, b = findClosestBrace(myexp)
    if a < 0 or b < 0:
        return evalexp(myexp)
    return evalwithBrackets(myexp[:a] + str(evalexp(myexp[a+1:b])) \
                            + myexp[b+1:])
        

def parseSimpExp(expStr):
    li = re.split("(\D+)", expStr.strip())
    if len(li) != 3:
        print "length not match"
        return
    a, ope, b = int(li[0]), li[1].strip(), int(li[2])
    if not operatorDict.has_key(ope):
        print ope, "not found"
        return
    return operatorDict[ope](a,b)

def iCal():
    print "Welcome to iCal version 0.1!"
    print "Type expression like 2+3*4/(4-3) and see the result."
    print "Type quit to exit"
    while True:
        s = raw_input(">> ")
        if s == "quit": return
        try:
            res = evalwithBrackets(s)
        except:
            res = "An error occured. Please check your expression"
        finally:
            print res

#explist = exp2list("3+4*2 - 6 / 2")
#print(explist)
#print(evalexp(explist))
#print evalwithBrackets("5+6*4*2 + 7/1*3")
#print evalwithBrackets("5+6*(4+ 3+1) + 7/(6-5)")
if __name__ == '__main__':
    iCal()

