import re

# "(+ 2 3)"  return tuple '2' '+' '3'
def parselisp(s):
    s = s.strip()
    if not (s[0] == "(" and s[-1] == ")"):
        print "not a valid expression"
        return
    s1 = s[1:-1]
    grp = filter(lambda x: x!= '',re.split(r"\s+", s1))    
    if len(grp) != 3:
        print "length not match"
        return
    return grp[1],grp[0],grp[2]

#"(+ 2 3)" => 5
def callisp(s):
    grp = parselisp(s)
    if grp == None:
        print "error"
        return
    return str(eval(''.join(grp)))

# "(+ 2 (* 3 4))" => (+ 2 12)
def parseOne(ss):
    if '(' not in ss: return ss
    length = len(ss)
    leftp, rightp = 0, 0
    for i in range(length):
        if ss[i] == "(":
            leftp = i
        elif ss[i] == ")":
            rightp = i
            subss = ss[leftp:(rightp+1)]
            news = callisp(subss)
            if news == None: return
            return ss[:leftp] + news + ss[rightp+1:]

def newlispinterpre(ss):
    if '(' not in ss: return ss
    subs = parseOne(ss)
    if subs == None: return
#    print subs
    return newlispinterpre(subs)

#interactive console
def iLisp():
    print "Welcome to iLisp beta 0.1. Have fun."
    print "Type exit to quit."
    while True:
        s = raw_input("iLisp: ")
        if s == "exit" or s == "quit":
            print 'Bye'
            return
        match = re.search(r"[A-Za-z_]", s)
        if not (match == None):
            print "Sorry. This version cannot manipulate variable."
            continue
        print newlispinterpre(s)
        

if __name__ == '__main__':
    iLisp()
