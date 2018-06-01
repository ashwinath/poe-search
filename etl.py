import tornado.ioloop
import tornado.web
import tornado.gen

from mediators.item_mediator import download_items
from es import es_factory

# does nothing
class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    es_factory.init_models()
    download_items()
    tornado.ioloop.IOLoop.current().start()
