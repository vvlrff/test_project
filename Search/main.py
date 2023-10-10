from elasticsearch import Elasticsearch
from db_postgres import PG_DB

from datetime import datetime

class IntellectualSearch:
   def __init__(self, elastic_url='http://localhost:9200') -> None:

      self.es = Elasticsearch(elastic_url)
      self.db = PG_DB()

   def date_convertor(self, date):
      return datetime.strptime(date, '%Y-%m-%d')
   
   def link_building(self, sender, message_id):
      return str(sender) + '/' + str(message_id)
   
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

  #  def main(self, querry, begin, end):

  #     begin = self.date_convertor(begin)
  #     end = self.date_convertor(end)
  #     elastic_answer = self.elastic_search(querry=querry, begin=begin, end=end)

  #     final_answer = []
  #     for el in elastic_answer:
  #        all_data = self.db.get_all_info(el['id'])

  #        element_for_front = {
  #                             'id': all_data['TG_DATA_ID'],
  #                             'relevant_score': el['relevant_score'],
  #                             'date': all_data['DATE'].strftime('%Y-%m-%d %H:%M:%S'),
  #                             'text': all_data['MESSAGE'],
  #                             'link_to_original': self.link_building(all_data['SENDER'], all_data['MESSAGE_ID']),
  #                             'photo_id': all_data['PHOTO_ID']
  #                             }

  #        final_answer.append(element_for_front)

  #     for el in final_answer:
  #        print(el)

  #     # print(final_answer)
  #     return final_answer

if __name__ == '__main__':
   search = IntellectualSearch()
   search.main('Удары по Донецку', '2023-10-09', '2023-10-10')
