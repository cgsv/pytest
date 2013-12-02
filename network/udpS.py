import socket, sys, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PORT = 1234

if len(sys.argv) == 2: 
    network = 'localhost'
    filename = sys.argv[1]
    f = open(filename, "rb")
    transrate = 21100  #kbps
    sleeptime = 188.0 * 8 * 10 / transrate / 1000 
    while True:
        buf = f.read(1880)
        if buf == '':
            break
        s.sendto(buf, (network, PORT))
        time.sleep(sleeptime)
    f.close()
