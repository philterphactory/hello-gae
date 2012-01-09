from google.appengine.ext.webapp.util import run_wsgi_app


STATUS = '200 OK'
CONTENT = '<html><head><title>Hello, world!</title></head><body><h1>Hello, world!</h1></html>'
CONTENT_LENGTH = len(CONTENT)
RESPONSE_HEADERS = [
    ('Content-Type', 'text/html'),
    ('Content-Length', str(CONTENT_LENGTH)),
    ('Cache-Control', 'public, max-age=60')
]


def application(environ, start_response):
    start_response(STATUS, RESPONSE_HEADERS)
    return [CONTENT]


if __name__ == '__main__':
    run_wsgi_app(application)
