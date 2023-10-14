from elasticsearch import Elasticsearch


class IntellectualSearch:
    def __init__(self, elastic_url='http://localhost:9200') -> None:

      self.es = Elasticsearch(elastic_url)

    def drop_dublikates(self, elastic_answer):
        unique_texts = set()
        unique_results = []

        for el in elastic_answer:
            text = el['msg']
            if text not in unique_texts:
                unique_texts.add(text)
                unique_results.append(el)

        return unique_results
   
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
      elastic_answer = []
      for el in result['hits']['hits']:
          if el['_source']['photo'] == 'None':
            el['_source']['photo'] = "5253752555547251902"
          elastic_answer.append({'id': el['_source']['id'],
                                'date': el['_source']['date'],
                                'relevant_score': el['_score'],
                                'msg': el['_source']['content'],
                                'url': el['_source']['link'],
                                'photo': f"http://localhost:8001/Photos/image{el['_source']['photo']}.jpg"
                                })
          
    def main1(self, querry):
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
                            }
                          ]
                        }
                      }
                    }
      result = self.es.search(index="news_index", body=query_body)
      elastic_answer = []
      for el in result['hits']['hits']:
          if el['_source']['photo'] == 'None':
            el['_source']['photo'] = "5253752555547251902"
          elastic_answer.append({'id': el['_source']['id'],
                                'date': el['_source']['date'],
                                'relevant_score': el['_score'],
                                'msg': el['_source']['content'],
                                'url': el['_source']['link'],
                                'photo': f"http://localhost:8001/Photos/image{el['_source']['photo']}.jpg"
                                })
          
      return self.drop_dublikates(elastic_answer)


# if __name__ == '__main__':
#    search = IntellectualSearch()
#    print(search.main('яндекс', '2023-10-09 00:00:00', '2023-10-13 00:00:00'))
