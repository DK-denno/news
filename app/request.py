from app import app
import urllib.request
import json
from .config import Config
# from config import
from models import source, headlines

Sources = source.Sources
Headlines = headlines.Headlines

base_url = app.config['SOURCES_URL']
api_key = app.config['API_KEY']

headline_base_url = app.config['HEADLINES_URL']


def get_sources():
    full_url = base_url.format(api_key)
    with urllib.request.urlopen(full_url) as url:
        source_data = url.read()
        json_source_data = json.loads(source_data)
        # print(json_source_data)

        source_list = None

        if json_source_data['sources']:
            json_lib = json_source_data['sources']
            source_list = process_sources(json_lib)

    return source_list


def process_sources(sources):
    source_list = []
    for one_source in sources:
        id = one_source.get('id')
        name = one_source.get('name')
        url = one_source.get('url')
        country = one_source.get('country')

        data_sources = Sources(id, name, url, country)
        source_list.append(data_sources)
        # print('full_headlines_url')

    return source_list

