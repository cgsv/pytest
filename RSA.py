import math

def isprime(n):
    if n <= 1: return False
    if n == 2: return True
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nthPrime(n):
    if n <= 1: return 2
    pre = nthPrime(n-1)
    pre += 1
    while not isprime(pre): pre += 1
    return pre

def gcd(a,b):
    if a % b == 0: return b
    return gcd(b, a % b)

def getfactor(n):
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return [i] + getfactor(n/i)
    return [n]

def testKey(publicKey, privateKey):
    n1,e1 = publicKey
    n2,e2 = privateKey
    if n1 != n2: return False
    nfac = getfactor(n1)
    if len(nfac) != 2: return False
    p, q = nfac
    m = (p-1) * (q-1)
    if gcd(e1, m) != 1: return False
    if e1 * e2 % m != 1: return False
    return True

def tryCrack(publicKey, count, e2s = 0):
    n, e1 = publicKey
    nfac = getfactor(n)
    if len(nfac) != 2:
        print "key error"
        return
    p, q = nfac
    m = (p -1) * (q -1)
    if gcd(e1, m) != 1:
        print "key error2"
        return
    e2list = []
    e2 = e2s
    while True:
        e2 += 1
        if e1 * e2 % m == 1:
            e2list.append(e2)
            if len(e2list) > count:
                return e2list

def getKeyBy2Prime(p, q, e1s = 201, e2s = 201):
    if not isprime(p) or not isprime(q):
        print "Parameters must be prime numbers"
        return
    n = p * q
    m = (p - 1) * (q - 1)
    e1 = e1s
    while gcd(e1, m) != 1: e1 += 1
    e2 = e2s
    while e1 * e2 % m != 1: e2 += 1
    return [n, e1], [n, e2]    

def enc(a, Key):
    return a**Key[1] % Key[0]

def encStr(s, Key):
    es = ''
    for si in s:
        es += chr(enc(ord(si), Key))
    return es

if __name__ == '__main__':
    pubKey = [77, 13]
    priKey = [77, 37]
    print testKey(priKey,pubKey)
    #print filter(isprime, range(200))
    pub, pri = getKeyBy2Prime(13, 19, 60, 60)
    print pub, pri
    print tryCrack(pub, 10)
    print testKey(pub, pri)

    mynum = 142
    emynum = enc(mynum, pub)
    dmynum = enc(emynum, pri)
    print mynum, emynum, dmynum

    greet = "hello, cgsv!"
    egreet = encStr(greet, pub)
    dgreet = encStr(egreet, pri)
    print greet, egreet, dgreet
    print [nthPrime(i) for i in range(300,303)]
    k1, k2 = getKeyBy2Prime(nthPrime(200), nthPrime(300))
    print k1, k2
    print tryCrack(k1, 10)

