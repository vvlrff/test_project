from elasticsearch import Elasticsearch
from db_postgres import PG_DB

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
                                  "fuzziness": 3
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

      elastic_answer = []

      for el in result['hits']['hits']:
         elastic_answer.append({'id': el['_source']['id'],
                                'date': el['_source']['date'],
                                'relevant_score': el['_score'],
                                'text': el['_source']['content'],
                                'link': el['_source']['link'],
                                'photo_id': el['_source']['photo']})

      for el in elastic_answer:
         print(el)
         
      return elastic_answer


if __name__ == '__main__':
   search = IntellectualSearch()
   search.main('Удары по Донецку', '2023-10-09 00:00:00', '2023-10-10 00:00:00')
