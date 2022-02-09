import requests, json, os
from elasticsearch import Elasticsearch

directory = '/media/ashu/New Volume1/Elasticsearch-main/'
res = requests.get('http://192.168.1.17:9200')
print (res.content)
es = Elasticsearch([{'host': '192.168.1.17', 'port': '9200'}])
i = 1
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(filename)
        docket_content = f.read()
        # Send the data into es
        es.index(index='cveindex', ignore=400, doc_type='docket', 
        cveid=i, body=json.loads(docket_content))
        i = i + 1
