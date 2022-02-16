from xml.dom.minidom import Document
import requests, os
import simplejson as json
from elasticsearch import Elasticsearch
filename = '/home/ashu/Documents/elasticsearch/Elasticsearch/csvjson.json'
res = requests.get('http://192.168.1.17:9200')
print (res.content)
es = Elasticsearch([{'host': '192.168.1.17', 'port': '9200'}])
es.indices.create(index="cveindex",ignore=[400,404])
if es.indices.exists(index="cveindex") is False: 
    es.indices.create(index="cveindex" , ignore=400)
f = open(filename,'r')
data= json.load(f)
j=1
ed={}
for attr,value in data.items(): 
    ed[j] = {attr: value}
    j +=1
    # Send the data into es
doc=data
es.index(index='cveindex', ignore=400, doc_type='document', id=j, document=doc)     
data = es.search(index="cveindex",query={"match":{'cveid': 'CVE-2020-18442'}})
ds = es.search(index="cveindex", ignore=400 ,query={"match":{"cveid":"CVE-2020*"}})
all = es.search(index="cveindex", ignore=400 ,query={"match_all":{}})
print (data)
