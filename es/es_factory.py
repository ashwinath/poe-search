import context
import tornado.gen

from .generic_item import GenericItemStore

@tornado.gen.coroutine
def init_models():
    generic_item_store = GenericItemStore()
    yield generic_item_store.init_mappings()
    context.set_dependency(generic_item_store)
