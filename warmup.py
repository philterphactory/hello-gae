from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import memcache


class HelloWorld(db.Model):
    content = db.StringProperty(required=True, indexed=False)


def application(environ, start_response):
    content = '<html><head><title>Hello, world!</title></head><body><h1>Hello, world!</h1></html>'

    key_name = "1"
    HelloWorld.get_or_insert(key_name, content=content)

    key = 'miniapp__hellomemcache'
    memcache.add(key, content, time=60)

    start_response(STATUS, [])
    return ['OK']


if __name__ == '__main__':
    run_wsgi_app(application)
