import socket, sys, launcelot

def client(hostname, port):
    s = socket.socket()
    s.connect((hostname, port))
    s.sendall(launcelot.qa[0][0])
    ans1 = launcelot.recv_until(s, '.')
    s.sendall(launcelot.qa[1][0])
    ans2 = launcelot.recv_until(s, '.')
    s.sendall(launcelot.qa[2][0])
    ans3 = launcelot.recv_until(s, '.')
    s.close()
    print ans1
    print ans2
    print ans3

if __name__ == '__main__':
    client('localhost', 1060)

