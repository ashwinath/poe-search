import tornado.gen
import tornado.escape

from tornado.httpclient import AsyncHTTPClient

class ElasticSearchTemplate(object):
    BASE_ELASTIC_SEARCH_URL = "http://localhost:9200"

    @tornado.gen.coroutine
    def init_mappings(self):
        """
        Requires a MAPPING and INDEX variable
        """
        if hasattr(self, "MAPPING") and hasattr(self, "INDEX"):
            http_client = AsyncHTTPClient()
            # always reindex
            yield http_client.fetch(
                    "{}/{}".format(self.BASE_ELASTIC_SEARCH_URL, self.INDEX),
                    method="DELETE",
                    raise_error=False)

            # create index
            response = yield http_client.fetch(
                    "{}/{}".format(self.BASE_ELASTIC_SEARCH_URL, self.INDEX),
                    method="PUT",
                    body=tornado.escape.json_encode(self.MAPPING),
                    headers= {"Content-Type": "application/json"},
                    raise_error=False)
            if response.code != 200:
                raise Exception("ElasticSearch error: {}".format(response.body))
