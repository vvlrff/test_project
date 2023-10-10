from elasticsearch import Elasticsearch
from .db_postgres import PG_DB

from datetime import datetime

class IntellectualSearch:
   def __init__(self, elastic_url='http://localhost:9200') -> None:

      self.es = Elasticsearch(elastic_url)
      self.db = PG_DB()

   def date_convertor(self, date):
      return datetime.strptime(date, '%Y-%m-%d')

   def date_checking(self, begin, end, post_date):
      return begin <= post_date <= end
   
   def link_building(self, sender, message_id):
      return str(sender) + '/' + str(message_id)
   
   def elastic_search(self, querry):
      query_body = {
         "query": {
            "match": {
               "content": {
                  "query": querry,
                  "operator": "and",
                  "fuzziness": 3
               }
            }
         }
      }

      result = self.es.search(index="news_index", body=query_body)
      elastic_answer = []
      for el in result['hits']['hits']:
         elastic_answer.append({'relevant_score': el['_score'], 'id': el['_source']['id'], 'text': el['_source']['content']})

      return elastic_answer

   def main(self, querry, begin, end):

      begin = self.date_convertor(begin)
      end = self.date_convertor(end)
      elastic_answer = self.elastic_search(querry=querry)

      final_answer = []
      for el in elastic_answer:
         post_date = self.db.is_post_in_time_range(el['id'])
         if self.date_checking(begin, end, post_date):
            all_data = self.db.get_all_info(el['id'])

            if all_data['PHOTO_ID'] == None:
               all_data['PHOTO_ID'] = "5253752555547251902"

            element_for_front = {
                                 'id': all_data['TG_DATA_ID'],
                                 'relevant_score': el['relevant_score'],
                                 'date': all_data['DATE'].strftime('%Y-%m-%d %H:%M:%S'),
                                 'msg': all_data['MESSAGE'],
                                 'url': self.link_building(all_data['SENDER'], all_data['MESSAGE_ID']),
                                 'photo': f"localhost:8000/Photos/{'image'}{all_data['PHOTO_ID']}.jpg"
                                 }

            # print(element_for_front['photo_id'])
            final_answer.append(element_for_front)

      # for el in final_answer:
      #    print(el)

      # print(final_answer)
      return final_answer

# if __name__ == '__main__':
#    search = IntellectualSearch()
#    search.main('Прилеты в городах', '2023-10-07', '2023-10-09')
