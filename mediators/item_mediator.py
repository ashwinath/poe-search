import tornado.gen

from bs4 import BeautifulSoup
from tornado.httputil import url_concat
from utils.download import download

BASE_URL = "https://pathofexile.gamepedia.com/api.php"

# TODO: need to find out list of projetions
PROJECTIONS = [
    "name",
    "class",
    "base_item",
    "implicit_stat_text",
    "explicit_stat_text",
    "drop_level",
    "drop_level_maximum",
    "required_dexterity",
    "required_intelligence",
    "required_level",
    "required_level_base",
    "required_strength",
    "base_item",
]

PARAMS = {
    'action': 'cargoquery',
    "format": "json",
    'tables': 'items',
    'fields': ",".join(PROJECTIONS),
    'where': 'class<>"Microtransactions"',
    "group_by": "name",
    "order_by": "name",
    "limit": 0, # to be replaced
    "offset": 0, # to be replaced
}


@tornado.gen.coroutine
def download_items():
    counter = 0
    step = 100

    while True:
        PARAMS["limit"] = step
        PARAMS["offset"] = counter
        url = url_concat(BASE_URL, PARAMS)
        response = yield download(url)
        list_of_items = response.json_body.get("cargoquery", [])
        for item in list_of_items:
            # implicit
            raw_html_implicit_stat = item['title']['implicit stat text']
            sanitised_implicit_stat = sanitise_text(raw_html_implicit_stat)
            item['title']['implicit stat text'] =sanitised_implicit_stat

            # explicit
            raw_html_explicit_stat = item['title']['explicit stat text']
            sanitised_explicit_stat = sanitise_text(raw_html_explicit_stat)
            item['title']['explicit stat text'] =sanitised_explicit_stat

        # TODO: Store into elastic search

        if len(list_of_items) == 0:
            break

        counter += step

def sanitise_text(html_text):
    return "".join(BeautifulSoup(html_text, "html.parser").findAll(text=True)).split('<br>')
