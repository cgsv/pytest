import random
import os
import glob
import collections
import pprint

def checkequal(te,teck,varlist):
    for m in varlist:
        if te(m) != teck(m): return False
    return True

def getRandomList(amin, amax, count):
    res = []
    for i in range(count):
        res.append(random.randint(amin,amax))
    return res

def getFileList(path):
    pa = path.strip()
    if pa[-1] != "/": pa = pa + "/"
    return glob.glob(pa + "*.py")

def checkHomework(funname, checkfunname, folder):
    def testfcheck2(n):
        return n * n * n
    resdict = {}
    for m in getFileList(folder):
        msg = ''
        if locals().has_key(funname):
            del locals()[funname]
        try:
            execfile(m)
        except:
            print m, ":", "the file has syntax error"
            resdict[m] = "syntax_error"
            continue
        if not locals().has_key(funname):
            msg = "Cannot find the funciton testff"
            resdict[m] = "function_not_found"
        else:
            testf = locals()[funname]
            testfcheck = locals()[checkfunname]
            status = checkequal(testf, testfcheck, getRandomList(0,1000,50))
            if status:
                msg = "test passed"
                resdict[m] = "right"
            else:
                msg = "testff is found but not right"
                resdict[m] = "funciton_wrong"
        print m, ":", msg

    print
    pprint.pprint(resdict)
    print
    pprint.pprint(collections.Counter(resdict.values()).items())    

if __name__ == '__main__':
    checkHomework('testff', 'testfcheck2', "homework")

            
        


    
    
