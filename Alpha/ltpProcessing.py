#encoding:utf-8#
'''
Created on 2017.8.21

@author: ZhongqiLi
'''
import re
import os
import SETTINGS
from googleTrans import googleTranslatror
from pyclausie import ClausIE
from SPtuple import SPtulpe
from dataReader import dataReader
from pyltp import SentenceSplitter,Segmentor,Postagger,Parser,SementicRoleLabeller,NamedEntityRecognizer
class ltpProcessor(object):
    
    def __init__(self,):
        LTP_DATA_DIR = SETTINGS.LTP_DATA_DIR # ltp模型目录的路径
        cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
        pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
        par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
        srl_model_path = os.path.join(LTP_DATA_DIR, 'srl')  # 语义角色标注模型目录路径，模型目录为`srl`。注意该模型路径是一个目录，而不是一个文件。
        ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
    
        self.segmentor = Segmentor()  # 初始化实例
        self.segmentor.load_with_lexicon(cws_model_path,'./segName')  # 加载模型
        self.postagger = Postagger() # 初始化实例
        self.postagger.load_with_lexicon(pos_model_path,'./postagName')  # 加载模型
        self.parser = Parser() # 初始化实例
        self.parser.load(par_model_path)  # 加载模型
        self.labeller = SementicRoleLabeller() # 初始化实例
        self.labeller.load(srl_model_path)  # 加载模型
        self.recognizer = NamedEntityRecognizer() # 初始化实例
        self.recognizer.load(ner_model_path)  # 加载模型
    
    def enumerateWordSeg(self,keyword=None,maxTweet = 99999,reader = dataReader()):
        reader = reader
        c = reader.cursor_tweet(keyword)
        tweetContent = []
        for tweetIndex,item in enumerate(c):  
            
            print tweetIndex+1,':'
            content =  item['Content'].replace(u'\u200b','')
            content = content.replace(u'\xa0','')
            content = content.replace(u'\u5168\u6587','')            
            content = content.encode('utf-8')
            content = re.sub(r'#.*?#|@.*?\s|\[.*?\]|\s|【|】|全文|的秒拍视频|(|)|“|”','',content)
            
            print content
            tweetContent.append(' '.join(self.segmentor.segment(content)))
            if tweetIndex+1 == maxTweet:
                break             
        return tweetContent

    def enumerateSPtuples_Translate(self,keyword=None,maxTweet = 99999,reader = dataReader()):
        reader = reader
        c = reader.cursor_tweet(keyword)
        tweetContent = {}
        SPtuples = []
        translator = googleTranslatror() 
        cl = ClausIE.get_instance(jar_filename='./clausie/clausie.jar')
        for tweetIndex,item in enumerate(c):  
            print tweetIndex+1,':'
            content =  item['Content'].replace(u'\u200b','')
            content = content.replace(u'\xa0','')
            content = content.replace(u'\u5168\u6587','')            
            content = content.encode('utf-8')
            content = re.sub(r'#.*?#|@.*?\s|\[.*?\]|\s|【|】|全文|的秒拍视频|(|)|“|”','',content)
            print content
            content = translator.translate_zhCN2en(content)
            print content
                    
            if tweetIndex+1 == maxTweet:
                break             
        return tweetContent,SPtuples
    
    
    def enumerateSPtuples(self,keyword=None,maxTweet = 99999,reader = dataReader()):
        reader = reader
        c = reader.cursor_tweet(keyword)
        tweetContent = {}
        SPtuples = []
        for tweetIndex,item in enumerate(c):  
            '''
            Use for Tweet2016 data clean
            
            content =  re.sub(r'<a.*?/a>|<i.*?/i>|<span.*?>|</span>|<br.*>|</br>|<img.*?>|#|\[.*?\]','',item['Content']+ ';' +item['TweetContent_repost'])
            content = re.sub(r'//:',';',content)
            
            END
            '''
            print tweetIndex+1,':'
            content =  item['Content'].replace(u'\u200b','')
            content = content.replace(u'\xa0','')
            content = content.replace(u'\u5168\u6587','')            
            content = content.encode('utf-8')
            content = re.sub(r'#.*?#|@.*?\s|\[.*?\]|\s|【|】|全文|的秒拍视频|(|)|“|”','',content)
            print content
            
            sents = SentenceSplitter.split(content)
            tweetContent[tweetIndex] = content
            
            for sent in sents:
                words = self.segmentor.segment(sent)
                postags = self.postagger.postag(words)
                netags = self.recognizer.recognize(words, postags)  # 命名实体识别
                arcs = self.parser.parse(words, postags)
                roles = self.labeller.label(words, postags, netags, arcs)  # 语义角色标注
        #    Processing data print:
#                 print sent
#                 print list(words)[-2]
#                 for j in range(0,len(words)):
#                     print j,'\t',
#                 print
#                 print '\t'.join(words)
#                 print '\t'.join(postags)
#                 print '\t'.join(netags)
#                 print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
        #    End
                for role in roles:
                    subject = [[arg.name, list(words[arg.range.start:arg.range.end+1])] for arg in role.arguments if arg.name in ['A0','A1','A2']]
                    if len(subject) > 0:
                        print 'Predicate:',words[role.index],":",'Subject:',
                        p = ''.join(words[role.index])
                        s = ''
                        for r in subject:
                            for text in r[1]:
                                print text,
                            print ';',
                            s = s +' '.join(r[1])
                        print
                        SPtuples.append(SPtulpe(p,s,tweetIndex))
                    
            if tweetIndex+1 == maxTweet:
                break             
        return tweetContent,SPtuples


    
