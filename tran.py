A = 'hit'
B = 'cog'
Dict = ['hot', 'dot', 'dog', 'lot', 'log']

def difnum(a, b):
    ret = 0
    for i in range(len(a)):
        if a[i] != b[i]: ret += 1
    return ret

def trans(a, b, mdict):
    if a == b: return []
    if difnum(a,b) == 1: return [[a, b]]
    res = []
    for m in mdict:
        if difnum(a,m) == 1 and difnum(a,b) >= difnum(m,b):
            res1 = trans(m, b, filter(lambda x: x != a, mdict))
            if res1 != []:
                res.extend(map(lambda x: [a] + x, res1))
    return res

def myfilter(res):
    a = min(map(lambda x:len(x), res))
    return filter(lambda x: len(x) == a,res)

print myfilter(trans(A, B, Dict))
