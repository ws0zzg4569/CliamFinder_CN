#encoding:utf-8
'''
Created on 2017.8.27

@author: ZhongqiLi
'''
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from ltpProcessing import ltpProcessor
import SETTINGS,pickle


class LDAparser(object):
    
    def __init__(self,corpus):
        self.corpus = corpus
        
    def fit(self,n_topics=5,learning_offset=50.,random_state=0):
        stpw = pickle.load(open(SETTINGS.Stplst_pth,'rb'))
#         cntVector = CountVectorizer(stop_words=stpw)
        cntVector = CountVectorizer()
        cntTf = cntVector.fit_transform(self.corpus)  
        
        print cntTf 
        lda = LatentDirichletAllocation(n_topics,learning_offset,random_state)
        docres = lda.fit_transform(cntTf)
        return docres
# USAGE EXAMPLE:
ltpProcessor = ltpProcessor() #Getting data and run ltp to corpus
corpus = ltpProcessor.enumerateWordSeg(maxTweet=100)
 
for c in corpus:
    print c
 
lda = LDAparser(corpus)
 
print lda.fit(n_topics=12)