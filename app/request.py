from app import app
import urllib.request,json

url = app.config['SOURCES_URL']
api = app.config['api']
def get_sources():
    full_url = url.format(api)
    with urllib.request.urlopen(full_url) as url:
        source = url.read()
        json_source = json.loads(source)

        sources = None
        
        if json_source['results']:
            json_lib = json_source['result']
            sources = process_sources(json_lib)
    return sources

def process_sources(sources):
    sources = []
    

            