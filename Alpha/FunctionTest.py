#encoding:utf-8
'''
Created on 2017.8.27
@author: ZhongqiLi
'''
from ltpProcessing import ltpProcessor
# from featureExraction import featureEctractor
# from wordcloud import WordCloud
# import pickle

# ltpProcessor = ltpProcessor() #Getting data and run ltp to corpus
# tweetContent,SPtuples = ltpProcessor.enumerteSPtuples('九寨',maxTweet=100)

# spts = SPtuples
# predicate_corpus = ''
# subject_corpus = ''
# for spt in spts:
#     predicate_corpus += ' ' + spt.ptedicate_str 
#     subject_corpus += ' ' + spt.subject_str
#     
# # Generate a word cloud image
# print predicate_corpus
# font = './font/msyh.ttf'
# wordcloud = WordCloud(collocations=False,font_path=font,width = 1400,height=1400).generate(unicode(subject_corpus, encoding='utf8'))
# 
# # Display the generated image:
# # the matplotlib way:
# import matplotlib.pyplot as plt
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# 
# plt.show()
ltpProcessor = ltpProcessor()
tweetContent,SPtuples = ltpProcessor.enumerateSPtuples_Translate('九寨',maxTweet=100)