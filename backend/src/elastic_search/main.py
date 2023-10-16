from elasticsearch import Elasticsearch
from ..config import ELASTIC_URL

class IntellectualSearch:
    def __init__(self, elastic_url='http://localhost:9200') -> None:
    # def __init__(self, elastic_url=ELASTIC_URL) -> None:
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
    
    def answer_transformation(self, result):
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
        return self.answer_transformation(result=result)

    def main_without_date(self, querry):
        query_body_without_date = {
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
        result = self.es.search(index="news_index", body=query_body_without_date)
        return self.answer_transformation(result=result)
    
    def sort_answer(self, querry: str, begin: str, end: str, param: str):
        result = self.main(querry=querry, begin=begin, end=end)
        if param == 'old':
            result = sorted(result, key=lambda x: x['date'])
        if param == 'new':
            result = sorted(result, key=lambda x: x['date'], reverse=True)
        if param == 'min_relevant_score':
            result = sorted(result, key=lambda x: x['relevant_score'])
        if param == 'max_relevant_score':
            result = sorted(result, key=lambda x: x['relevant_score'], reverse=True)
        return result
    
    def sort_answer_without_date(self, querry: str, param: str):
        result = self.main_without_date(querry=querry)
        if param == 'old':
            result = sorted(result, key=lambda x: x['date'])
        if param == 'new':
            result = sorted(result, key=lambda x: x['date'], reverse=True)
        if param == 'min_relevant_score':
            result = sorted(result, key=lambda x: x['relevant_score'])
        if param == 'max_relevant_score':
            result = sorted(result, key=lambda x: x['relevant_score'], reverse=True)
        return result
        



# if __name__ == '__main__':
#    search = IntellectualSearch()
#    print(search.main('яндекс', '2023-10-09 00:00:00', '2023-10-13 00:00:00'))
