import tornado.gen
import tornado.escape

from tornado.httpclient import AsyncHTTPClient

@tornado.gen.coroutine
def download(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    if response.code == 200:
        response.json_body = tornado.escape.json_decode(response.body)

    return response
