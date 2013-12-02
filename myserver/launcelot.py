import socket, sys
PORT = 1060
qa = (('What is your name?', 'My name is Sir Launcelot of Camelot.'),
    ('What is your quest?', 'To seek the Holy Grail.'),
    ('What is your favorite color?', 'Blue.'))
qadict = dict(qa)

def recv_until(sock, suffix):
    message = ''
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise EOFError('socket closed')
        message += data
    return message

def setup():
    interface = sys.argv[1] if len(sys.argv) == 2 else 'localhost'
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, PORT))
    sock.listen(128)
    print 'Ready and listening at %r port %d' % (interface, PORT)
    return sock
