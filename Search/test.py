# # import requests
# # substring = 'You Know, for Search'.encode()
# # response = requests.get('http://127.0.0.1:9200')
# # if substring in response.content:
# #     print('Elasticsearch is up and running!')
# # else:
# #     print('Something went wrong, ensure the cluster is up!')


# # from elasticsearch import Elasticsearch

# # es = Elasticsearch("http://localhost:9200")

# # mappings = {
# #         "properties": {
# #             "title": {"type": "text", "analyzer": "english"},
# #             "id": {"type": "integer"}
# #     }
# # }

# # es.indices.create(index="ai_news", mappings=mappings)


# # import requests
# # from elasticsearch import Elasticsearch
# # substring = 'You Know, for Search'.encode()
# # response = requests.get('http://127.0.0.1:9200')
# # if substring in response.content:
# #     es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


# # from datetime import datetime
# # from elasticsearch import Elasticsearch
# # es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# # doc = {
# # 'author': 'document-author',
# # 'text': 'A text document',
# # 'timestamp': datetime.now()
# # }
# # res = es.index(index='sample-index', id=2, body=doc)
# # print(res['result'])


# from elasticsearch import Elasticsearch
# import logging

# def connect_elasticsearch():
#     _es = None
#     _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#     if _es.ping():
#         print('Yay Connect')
#     else:
#         print('Awww it could not connect!')
#     return _es

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.ERROR)


# def create_index(es_object, index_name='recipes'):
#     created = False
#     # index settings
#     settings = {
#         "settings": {
#             "number_of_shards": 1,
#             "number_of_replicas": 0
#         },
#         "mappings": {
#             "members": {
#                 "dynamic": "strict",
#                 "properties": {
#                     "title": {
#                         "type": "text"
#                     },
#                     "submitter": {
#                         "type": "text"
#                     },
#                     "description": {
#                         "type": "text"
#                     },
#                     "calories": {
#                         "type": "integer"
#                     },
#                 }
#             }
#         }
#     }
#     try:
#         if not es_object.indices.exists(index_name):
#             # Ignore 400 means to ignore "Index Already Exist" error.
#             es_object.indices.create(index=index_name, ignore=400, body=settings)
#             print('Created Index')
#         created = True
#     except Exception as ex:
#         print(str(ex))
#     finally:
#         return created

# def store_record(elastic_object, index_name, record):
#     try:
#         outcome = elastic_object.index(index=index_name, doc_type='salads', body=record)
#     except Exception as ex:
#         print('Error in indexing data')
#         print(str(ex))
    

# # create_index(connect_elasticsearch())
# print(connect_elasticsearch().get(index="recipes", id="my_document_id"))


from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')

es.index(index='my_index3', doc_type='my_index', id=3, document={'text': 'mobile phone'})
es.index(index='my_index3', doc_type='my_index', id=4, document={'text': 'apple'})


# print(es.search(index='my_index', doc_type='my_index', body={'query': {'match': {'text': 'this test'}}}))
print(es.search(index='my_index3', doc_type='my_index', document={'query': {'match': {'text': 'phone'}}}))
