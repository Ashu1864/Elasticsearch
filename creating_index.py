from elasticsearch import Elasticsearch
##setup connection
es=Elasticsearch([{"host":"localhost","port":9200}])
print(es.ping())
##create index
es.indices.create(index="elasticsearch_index")
##display all indices
indices=es.indices.get_alias("*")
for index in indices:
    print(index)