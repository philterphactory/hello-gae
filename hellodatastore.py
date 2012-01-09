from google.appengine.ext import db


CONTENT = '<html><head><title>Hello, world!</title></head><body><h1>Hello, world!</h1></html>'
STATUS = '200 OK'


class HelloWorld(db.Model):
    content = db.StringProperty(required=True, indexed=False)


def application(environ, start_response):
    key_name = "1"
    obj = HelloWorld.get_or_insert(key_name, content=CONTENT)
    
    content_length = len(obj.content)
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(content_length))
    ]
    start_response(STATUS, response_headers)
    return [str(obj.content)]
