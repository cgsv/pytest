import sys

def catfile(jpgfile, otherfile, outfile):
    f1 = open(jpgfile, "rb")
    f2 = open(otherfile, "rb")
    f3 = open(outfile, "wb")
    f3.write(f1.read())
    f3.write(f2.read())
    f1.close()
    f2.close()
    f3.close()

def splitfile(infile, outjpg, outother):
    f1 = open(infile, 'rb')
    buf = f1.read()
    f1.close()
    pos = buf.find('\xff\xd9')
    if pos < 0:
        f1.close()
        print "Error jpg format"
        return
    with open(outjpg, "wb") as f2:
        f2.write(buf[:pos+2])
    with open(outother, "wb") as f3:
        f3.write(buf[pos+2:])

def printUsage():
    print "Usage: python jpgPre.py cat in1.jpg in2.txt out.jpg"
    print "or python jpgPre.py split in.jpg out1.jpg out2.txt"

if __name__ == '__main__':
    if len(sys.argv) != 5:
        printUsage()
        exit()
    if sys.argv[1] == 'cat':
        catfile(*sys.argv[2:5])
    elif sys.argv[1] == 'split':
        splitfile(*sys.argv[2:5])
    else:
        printUsage()

