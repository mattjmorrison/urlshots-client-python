import time
import logging
import unittest
from urlshots import API
import multiprocessing
from wsgiref.simple_server import WSGIServer, WSGIRequestHandler


class ApiTests(unittest.TestCase):

    def setUp(self):
        logging.getLogger('urlshots').setLevel('ERROR')
        logging.getLogger('urllib3.connectionpool').setLevel('ERROR')
        self.p = multiprocessing.Process(target=ApiTests.server)
        self.p.daemon = True
        self.p.start()

    def tearDown(self):
        self.p.terminate()

    @classmethod
    def server(cls):
        server = WSGIServer(('localhost', 8999), WsgiHandler)
        server.set_app(cls.wsgi_app)
        server.serve_forever()

    @staticmethod
    def wsgi_app(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return ['Hello']

    def test_working(self):
        from urllib2 import urlopen
        self.assertEqual("Hello", urlopen('http://localhost:8999/render?url=http://joel.io').read())

    def test_image(self):
        response = API(host="http://localhost:8999", timeout=3).image('http://joel.io')
        self.fail("Response: '{}'".format(response))


class WsgiHandler(WSGIRequestHandler):

    def log_message(self, *args):
        "Do not log to keep clean test output"


if __name__ == '__main__':
    unittest.main()
