import cgi, base64
from wsgiref.simple_server import make_server

def page(content, *args):
    yield '<html><head><title>cgsv simple web</title></head><body>'
    yield content % args
    yield '</body>'

def simple_app(environ, start_response):
    gohome = '<br><a href="/">Return home</a>'
    q = cgi.parse_qs(environ['QUERY_STRING'])

    if environ['PATH_INFO'] == '/':
        start_response('200 OK', [('Content-Type','text/html')])
        return page('Welcome! Enter a string: <form action="encode">'
                '<input name="mystring"><input type="submit"></form>')

    elif environ['PATH_INFO'] == '/encode':
        my = q['mystring'][0]
        start_response('200 OK', [('Content-Type','text/html')])
        return page('<tt>%s</tt> base64 encoded is: <tt>%s</tt>' + gohome,
                cgi.escape(repr(my)), cgi.escape(base64.b64encode(my)))

print "listening on localhost 80"
make_server('localhost', 1234, simple_app).serve_forever()
        
