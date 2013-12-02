import random
import string

def modfabi(n):
    a , b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a % 128
    
def getFabiChar():
    a = 0
    while True:
        ch = chr(modfabi(a))
        a += 1
        if ch in string.letters + string.digits: yield ch

def myfabiChar():
    a, b = 0, 1
    while True:
        ch = chr(a%128)
        if ch in string.letters + string.digits: yield ch
        a, b = b, a + b

def getRandChar():
    return random.choice(string.letters)

def writeRandomFile(filename, length):
    f = open(filename, "w")
    for i in range(length):
        f.write(getRandChar())
    f.close

def writeFabiRandomFile(filename, length):
    f = open(filename, "w")
    fabite = myfabiChar()
    for i in range(length):
        f.write(fabite.next())
    f.close

if __name__ == '__main__':
    writeFabiRandomFile("random.txt", 20000)
