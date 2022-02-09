import requests, json, os
from elasticsearch import Elasticsearch

directory = '/home/ashu/Documents/elasticsearch/Elasticsearch/'
res = requests.get('http://192.168.1.17:9200')
print (res.content)
es = Elasticsearch([{'host': '192.168.1.17', 'port': '9200'}])
check=es.indices.exists(index="cveindex")
print (check)
if check is True :
    i = 1
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            f = open(filename)
            docket_content = f.read()
            # Send the data into es
            es.index(index='cveindex', ignore=400, doc_type='docket', 
            id=i, body=json.loads(docket_content))
            i = i + 1
    data = es.get(index="cveindex", doc_type='docket', id=4)
    print(data)
else :
    es.indices.create(index="cveindex" , ignore=400)
    i = 1
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            f = open(filename)
            docket_content = f.read()
            # Send the data into es
            es.index(index='cveindex', ignore=400, doc_type='docket',
            id=i, body=json.loads(docket_content))
            i = i + 1
    data = es.get(index="cveindex", doc_type='docket', id=4)
    print(data)
