import socket, sys, random, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

MAX = 65535
PORT = 1234

if len(sys.argv) >=2 and sys.argv[1] == 'server':
    s.bind(('', PORT))
    print 'Listening for broadcasts at', s.getsockname()
    while True:
        data, address = s.recvfrom(MAX)
        print 'The client at %r says: %r' % (address, data)

elif len(sys.argv) == 3 and sys.argv[1] == 'client':
    network = sys.argv[2]
    f = open("D:/myfiles/document/upload/EVMTV_aa.vts", "rb")
    transrate = 2000 #kbps
    sleeptime = 188.0 * 8 * 10 / transrate / 1000 
    for i in range(100000):
        buf = f.read(1880)
        s.sendto(buf, (network, PORT))
        time.sleep(sleeptime)
    f.close()

else:
    print 'Usage'
    exit()
