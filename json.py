import simplejson as json 
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
i = 0
with open('nvd.json') as raw_data:
    json_docs = json.load(raw_data)
    for json_doc in json_docs:
            i = i + 1
            es.index(index='elasticsearch_index', doc_type='doc_dharan', id=i, body=json.dumps(json_doc))