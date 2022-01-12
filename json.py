import simplejson as json
from elasticsearch import Elasticsearch

es = Elasticsearch(host="localhost", port=9200)
with open('csvjson.json') as data_file:
    data = json.load(data_file)
    file = len(data)
    for results in data:
        for x in range(0, file):
            ind = results['result'][x]['cve/CVE_data_meta/ID']
            index = results['result'][x]
            es.indices.create(index=ind)
            es.index(index=ind, doc_type='CVE', id=ind, body=json.loads(index.content))
