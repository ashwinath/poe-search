import tornado.ioloop
import tornado.web
import tornado.gen

from mediators.item_mediator import download_items

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
    download_items()
    tornado.ioloop.IOLoop.current().start()
