#encoding:utf-8
'''
Created on 2017.8.22

@author: ZhongqiLi
'''
import pickle 
import SETTINGS
from SPtuple import SPtulpe   
from sklearn.feature_extraction.text import TfidfTransformer    
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.cluster import AgglomerativeClustering,SpectralClustering
import numpy as np



spts = pickle.load(open('./SPtuples','rb'))
print  'Loaded!',len(spts)
predicate_corpus = []
subject_corpus = []

for spt in spts:
    predicate_corpus.append(spt.ptedicate_str) 
    subject_corpus.append(spt.subject_str)


vectorizer = CountVectorizer()
transformer = TfidfTransformer()  

m = vectorizer.fit_transform(predicate_corpus)
tfidf = transformer.fit_transform(m) 
word = vectorizer.get_feature_names() 
weight = tfidf.toarray()
print len(word)
# print m
m = m.astype(bool).astype(int)
 
intrsct = m.dot(m.T)
row_sums = intrsct.diagonal()


unions = row_sums[:,None] + row_sums - intrsct
dist1 = SETTINGS.Omega * intrsct / unions




m = vectorizer.fit_transform(subject_corpus)
tfidf = transformer.fit_transform(m) 
word = vectorizer.get_feature_names() 
weight = tfidf.toarray()
# print len(word)

m = m.astype(bool).astype(int)

intrsct = m.dot(m.T)
np.set_printoptions(threshold='500')
row_sums = intrsct.diagonal()
unions = row_sums[:,None] + row_sums - intrsct
dist = (1.0 - SETTINGS.Omega) * intrsct / unions

simi = np.nan_to_num(dist1 + dist)
          
model_Agg = AgglomerativeClustering(affinity='precomputed',linkage='average',n_clusters=15)
model_Agg.fit(simi)
label =  model_Agg.labels_
print label
for i in range(len(model_Agg.labels_)):
    if label[i] == 0:
        print label[i],":",predicate_corpus[i],":",subject_corpus[i]
         
model_Spectral = SpectralClustering(affinity='precomputed',n_clusters=15)
model_Spectral.fit(simi)
label =  model_Spectral.labels_
np.set_printoptions(threshold='500')
print label
for i in range(len(model_Agg.labels_)):
    print label[i],":",predicate_corpus[i],":",subject_corpus[i]
    