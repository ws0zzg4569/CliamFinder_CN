#encoding:utf-8
'''
Created on 2017.8.24

@author: ZhongqiLi
'''
from ltpProcessing import ltpProcessor
from featureExraction import featureEctractor

if __name__ == '__main__':
    ltpProcessor = ltpProcessor() #Getting data and run ltp to corpus
    tweetContent,SPtuples = ltpProcessor.enumerateSPtuples('九寨',maxTweet=100)
    featureEctractor = featureEctractor(SPtuples)
    
    simi_matrix = featureEctractor.getSimilarityMatrix()
    print featureEctractor.clustering_Agglomerative(simi_matrix, 10)
    
    