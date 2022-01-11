import requests, json
from elasticsearch import Elasticsearch
res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch(host = "localhost", port = 9200)
with open('csvjson.json') as data_file:
    data = json.load(data_file)
    for result in data:
        print (result[result][0])