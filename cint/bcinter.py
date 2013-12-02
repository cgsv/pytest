import os
import platform
incFile = ['<stdio.h>', '<stdlib.h>', '<iostream>', '<vector>', '<algorithm>']
source_file = "tmp.cpp"
exe_file = "tmp"


def initWork():
    if os.path.isfile(source_file):
        os.remove(source_file)
    sys_exe = exe_file
    if platform.system() == 'Windows':
        sys_exe = sys_exe + ".exe"
    if os.path.isfile(sys_exe):
        os.remove(sys_exe)

def writeFile(slist, printitem):
    f = open(source_file, "w")
    for m in incFile:
        f.write("#include " + m + "\n")
    f.write("using namespace std;\n")
    f.write("\n")
    f.write("int main()\n{\n")

    for s in slist:
        f.write("\t" + s + "\n")
    if printitem != '':
        f.write("\tcout << " + printitem + " << endl;\n")    
    f.write("}");
    f.close()

def compileAndRunFile():
    cmd = "g++ -o " + exe_file + " " + source_file + " -std=c++11"
    pipe = os.popen(cmd)
    sts = pipe.close()
    if sts is None:
        return os.popen(exe_file).readlines(), 1
    else:
        return "Compile failed!", 0

def cint():
    print "Welcome to mini C++ interpreter."
    print "Type exit to quit."
    print "Type new to begin a new session"
    slist = []
    while True:
#        raw_input("wait")
        initWork()
        ustr = raw_input(">>")
        if ustr == 'exit':
            return
        if ustr == 'new':
            slist = []
            continue
        if ';' in ustr:
            slist.append(ustr)
            writeFile(slist,'')
            res = compileAndRunFile()
            if res[1] == 0:
                slist.pop()
                print res[0]
                continue
            if res[0] != []:
                for mr in res[0]:
                    print mr
            
        else:
            writeFile(slist, ustr)
            res = compileAndRunFile()
            if res[1] == 0:
                print res[0]
                continue
            print res[0][-1]
        
if __name__ == '__main__':
    cint()
        
