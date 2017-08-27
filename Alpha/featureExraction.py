#encoding:utf-8
'''
Created on 2017.8.22

@author: ZhongqiLi
'''
import SETTINGS,pickle
from SPtuple import SPtulpe   
from sklearn.feature_extraction.text import TfidfTransformer    
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.cluster import AgglomerativeClustering,SpectralClustering
import numpy as np

class featureEctractor(object):
    
    def __init__(self,SPtulpeSet):
        spts = SPtulpeSet
        self.predicate_corpus = []
        self.subject_corpus = []
        for spt in spts:
            self.predicate_corpus.append(spt.ptedicate_str) 
            self.subject_corpus.append(spt.subject_str)
        stpw = pickle.load(open(SETTINGS.Stplst_pth,'rb'))
        self.vectorizer = CountVectorizer(stop_words=stpw)
        self.transformer = TfidfTransformer()  
    
    def getSimilarityMatrix(self):
    
        m_predicate = self.vectorizer.fit_transform(self.predicate_corpus)
        m_subject = self.vectorizer.fit_transform(self.subject_corpus)
        
#         tfidf = self.transformer.fit_transform(m_predicate) 
#         word = self.vectorizer.get_feature_names() 
#         weight = self.tfidf.toarray()
#         print m
        m_predicate = m_predicate.astype(bool).astype(int)
        m_subject = m_subject.astype(bool).astype(int)
     
     
        intrsct_pre = m_predicate.dot(m_predicate.T)
        intrsct_sub = m_subject.dot(m_subject.T)
        
        row_sums_pre = intrsct_pre.diagonal()
        row_sums_sub = intrsct_sub.diagonal()
       
        unions_pre = row_sums_pre[:,None] + row_sums_pre - intrsct_pre
        unions_sub = row_sums_sub[:,None] + row_sums_sub - intrsct_sub
    
        simi_matrix = np.nan_to_num(SETTINGS.Omega * intrsct_pre / unions_pre + (1 - SETTINGS.Omega) * intrsct_sub / unions_sub)
        return simi_matrix

    def clustering_Agglomerative(self,semi_matrix,n_clusters = 15):              
        model_Agg = AgglomerativeClustering(affinity='precomputed',linkage='average',n_clusters=n_clusters)
        model_Agg.fit(semi_matrix)
        return model_Agg.labels_
    
    def clustering_Spectral(self,semi_matrix,n_clusters = 15):
        model_Spectral = SpectralClustering(affinity='precomputed',n_clusters=n_clusters)
        model_Spectral.fit(semi_matrix)
        return  model_Spectral.labels_
