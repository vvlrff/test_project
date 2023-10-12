from elasticsearch import Elasticsearch
from .db_postgres import PG_DB

from datetime import datetime

class IntellectualSearch:
   def __init__(self, elastic_url='http://localhost:9200') -> None:

      self.es = Elasticsearch(elastic_url)
   
   def main(self, querry, begin, end):
      query_body = {
                      "query": {
                        "bool": {
                          "must": [
                            {
                              "match": {
                                "content": {
                                  "query": querry,
                                  "operator": "and",
                                  "fuzziness": 'AUTO'
                            }
                              }
                            },
                            {
                              "range": {
                                "date": {
                                  "gte": begin,
                                  "lte": end
                                }
                              }
                            }
                          ]
                        }
                      }
                    }

      result = self.es.search(index="news_index", body=query_body)
      print(result)

      elastic_answer = []

      for el in result['hits']['hits']:
         print(el['_source']['photo'])
         if el['_source']['photo'] == 'None':
            el['_source']['photo'] = "5253752555547251902"
         elastic_answer.append({'id': el['_source']['id'],
                                
                                'date': el['_source']['date'],

                                'relevant_score': el['_score'],

                                'msg': el['_source']['content'],

                                'url': el['_source']['link'],

                                'photo': f"localhost:8000/Photos/image{el['_source']['photo']}.jpg"
                                })
      return elastic_answer

