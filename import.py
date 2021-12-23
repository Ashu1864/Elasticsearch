import requests, json, os
from elasticsearch import Elasticsearch
directory = 'D:\Python\React\test1.json'
res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
i = 1
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(filename)
        docket_content = f.read()
        # Send the data into es
        es.index(index='elasticsearch_index', ignore=400, doc_type='docket', 
        id=i, body=json.loads(docket_content))
        i = i + 1