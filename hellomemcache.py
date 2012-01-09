from google.appengine.api import memcache

STATUS = '200 OK'

def application(environ, start_response):
    key = 'miniapp__hellomemcache'
    content = memcache.get(key)
    if not content:
        content = '<html><head><title>Hello, world!</title></head><body><h1>Hello, world!</h1></html>'
        memcache.add(key, content, time=60)
    content_length = len(content)
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(content_length))
    ]
    start_response(STATUS, response_headers)
    return [content]
