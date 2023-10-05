# import os
# import gensim
# import string
# import numpy as np
# import pymorphy3
# import PyPDF2
# import re
# import nltk
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.metrics import silhouette_samples, silhouette_score
# from sklearn.cluster import KMeans
# from nltk.corpus import stopwords

# folder_path = os.getcwd() + r'\src\api\INPUT_\\'  # путь к папке, в которую нужно сохранить файл
# folder_nlp = os.getcwd() + r'\src\api\Model\\word2vec_300_100_3.bin'

# class Clusterization:
#     def __init__(self):
#         # Загрузка предобученной модели Word2Vec
#         model_path = folder_nlp
#         self.model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)

#         self.spec_chars = string.punctuation + r'\n\x0«»\t—…[]\n*'
#         self.stop_words = stopwords.words('russian')
#         self.morph = pymorphy3.MorphAnalyzer()

#     def pdf_converter(self, list_of_docs):
        
#         self.converted_texts = []

#         for path_to_pdf in list_of_docs:
#             # print(folder_path + path_to_pdf)
#             with open(folder_path + path_to_pdf, 'rb') as pdf_file:
#                 pdf_reader = PyPDF2.PdfReader(pdf_file)
#                 num_pages = len(pdf_reader.pages)
#                 text = ""
#                 if num_pages >= 7:
#                     num_pages = 7
#                     for page in range(num_pages):
#                         pdf_page = pdf_reader.pages[page]
#                         page_text = pdf_page.extract_text()
#                         text += page_text

#             self.converted_texts.append(text)

#     def preprocessing(self, converted_texts):
#         self.final_texts = []
#         for converted_text in converted_texts:
#             if converted_text is None:
#                 pass

#             if type(converted_text) != float:
#                 converted_text = "".join([ch for ch in converted_text if ch not in self.spec_chars])
#                 converted_text = re.sub('\n', '     ', converted_text)
#                 tokens = nltk.word_tokenize(converted_text)
#                 filtered_text = [word.lower() for word in tokens if word.lower() not in self.stop_words]
#                 self.final_text = []

#                 for word in filtered_text:
#                     if word.isalpha() and len(word) > 2:
#                         parsed_word = self.morph.parse(word)[0]
#                         # pos = parsed_word.tag.POS
#                         # self.final_text.append(f'{parsed_word.normal_form}_{pos}')
#                         self.final_text.append(parsed_word.normal_form)
#                     else:
#                         continue
            
#             self.final_texts.append(self.final_text)

#     def vectorize(self, list_of_docs, model):
#         self.vectorized_docs = []

#         for tokens in list_of_docs:
#             zero_vector = np.zeros(model.vector_size)
#             vectors = []
#             for token in tokens:
#                 # print(token)
#                 try:
#                     vectors.append(model[token])
#                 except KeyError:
#                     continue
#             if vectors:
#                 vectors = np.asarray(vectors)
#                 avg_vec = vectors.mean(axis=0)
#                 self.vectorized_docs.append(avg_vec)
#             else:
#                 self.vectorized_docs.append(zero_vector)
        

#     def find_opt_k(self, X):

#         all_nums, all_scores = [], []

#         for n_clusters in range(2, len(X)//2+1):
#             clusterer = KMeans(n_clusters=n_clusters)
#             preds = clusterer.fit_predict(X)
#             centers = clusterer.cluster_centers_

#             score = silhouette_score(X, clusterer.labels_)
#             all_nums.append(n_clusters)
#             all_scores.append(score)

#         max_score = max(all_scores)
#         # print("For n_clusters = {}, silhouette score is {})".format(all_nums[all_scores.index(max_score)], max_score))
#         # print(all_nums)
#         # print(all_scores)

#         return all_nums[all_scores.index(max_score)]

#     def kmeans_clusters(self, X, k, print_silhouette_values):

#         km = KMeans(n_clusters=k).fit(X)
#         labels = km.labels_
#         self.cluster_sizes = np.bincount(labels)

#         if print_silhouette_values:
#             sample_silhouette_values = silhouette_samples(X, km.labels_)
#             # print(f"Silhouette values:")
#             silhouette_values = []
#             for i in range(k):
#                 cluster_silhouette_values = sample_silhouette_values[km.labels_ == i]
#                 silhouette_values.append(
#                     (
#                         i,
#                         cluster_silhouette_values.shape[0],
#                         cluster_silhouette_values.mean(),
#                         cluster_silhouette_values.min(),
#                         cluster_silhouette_values.max(),
#                     )
#                 )
#             silhouette_values = sorted(
#                 silhouette_values, key=lambda tup: tup[2], reverse=True
#             )
#             # for s in silhouette_values:
#                 # print(
#                 #     f"    Cluster {s[0]}: Size:{s[1]} | Avg:{s[2]:.2f} | Min:{s[3]:.2f} | Max: {s[4]:.2f}"
#                 # )
#         return km, km.labels_

#     def find_diff_percent(self, doc_vectors):
#         self.sim_rates = []
#         for i in range(1, len(doc_vectors)):
#             similarity = cosine_similarity([doc_vectors[0]], [doc_vectors[i]])
#             # Преобразование к процентному значению
#             similarity_percent = (similarity[0][0] + 1) / 2 * 100
#             self.sim_rates.append(similarity_percent)
#             # print(f"Схожесть текстов 1 и {i+1}: {similarity_percent:.2f}%")
    
#     def main(self):

#         list_of_docs = os.listdir(path=folder_path)
#         # print(list_of_docs)
        
#         self.pdf_converter(list_of_docs)
#         self.preprocessing(self.converted_texts)
#         self.vectorize(self.final_texts, self.model)
#         # print(self.vectorized_docs)
#         opt_k = self.find_opt_k(self.vectorized_docs)
#         clustering, cluster_labels = self.kmeans_clusters(self.vectorized_docs, k = opt_k, print_silhouette_values = False)

#         self.descriptions = []
#         self.clust_size = []
#         final_clust = []

#         for i in range(opt_k):
#             tokens_per_cluster = ""
#             most_representative = self.model.most_similar(positive=[clustering.cluster_centers_[i]], topn=5)
#             for t in most_representative:
#                 tokens_per_cluster += f"{t[0]} "

#             self.clust_size.append(self.cluster_sizes[i])

#             most_representative_docs = np.argsort(np.linalg.norm(self.vectorized_docs - clustering.cluster_centers_[i], axis=1))
#             # print(most_representative_docs)
#             final_links = []

#             for d in most_representative_docs[:self.clust_size[i]]:
#                 final_links.append(list_of_docs[d])
            
#             # print(f'Current cluster num: {0}')
#             # print(f'Current cluster size: {len(self.final_links)}')
#             # print(self.final_links)

#             final_clust.append({'category':f'ОКС №{i+1}', 'description': tokens_per_cluster, 'amount': int(self.cluster_sizes[i]), 'file_names': final_links})

#             # print(f"Cluster {i}: {tokens_per_cluster}")
#             # self.descriptions.append(f'{i+1}) {tokens_per_cluster}')

#             # print(f'Amount of docs in clusters: {self.clust_size[i]}')

#         return final_clust

# if __name__ == '__main__':
#     cl = Clusterization()
#     print(cl.main())