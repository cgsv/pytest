import socket, sys
import threading, time


def server():
    global port1
    s = socket.socket()
    s.bind(('',port1))
    s.listen(1)
    conn, addr = s.accept() 
    while True:
        data = conn.recv(1024)
        if data == '': break
        print
        print '[%s:%d] send a message to me: %s'%(addr[0], addr[1], data)
    s.close

def client():
    global port2, ip
    c = socket.socket()
    c.connect((ip, port2))
    while True:
        sms = raw_input("Input the message: ")
        c.sendall(sms)
    c.close()

if __name__ == '__main__':
    port1 = int(sys.argv[1])
    port2 = int(sys.argv[2])
    ip = sys.argv[3]
    ser = threading.Thread(target=server)
    clt = threading.Thread(target=client)
    ser.start()
    time.sleep(5)
    clt.start()
    ser.join()
    clt.join()
    

# python chat.py 22222 33333 192.168.0.168
# python chat.py 33333 22222 192.168.0.168
