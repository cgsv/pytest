import socket

messages = [ "This is the message",
             "It will be sent",
             "in parts"]

print "Connect to the server"
server_address = ('localhost', 10001)

socks = []

for i in range(10):
    socks.append(socket.socket())

for s in socks:
    s.connect(server_address)

counter = 0

for message in messages:
    for s in socks:
        counter += 1
        print "  %s sending %s" % (s.getsockname(), message)
        s.send(message + " version "+str(counter))

    for s in socks:
        data = s.recv(1024)
        print " %s received %s" % (s.getsockname(),data)
        if not data:
            print "closing socket ", s.getsockname()
            s.close()
