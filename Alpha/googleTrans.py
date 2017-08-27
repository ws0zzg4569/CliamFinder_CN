#encoding:utf-8
'''
Created on 2017.8.25

@author: ZhongqiLi
'''
from googletrans import Translator


#zh-CN,en

class googleTranslatror(object):
    
    
    def __init__(self):
        self.translator = Translator() 
    
    def translate_en2zhCN(self,text):
        return self.translator.translate(text, src = 'en',dest = 'zh-CN').text
    
    def translate_zhCN2en(self,text):
        return self.translator.translate(text, src = 'zh-CN',dest = 'en').text
# USAGE EXAMPLE:   
# translator = Translator()
# for i in range(10):
#     translations = translator.translate(['#早安#  知道这是做啥吗[doge]','滴，周五卡！ ​​​'])
#     for translation in translations:
#         print translation.origin, ' -> ', translation.text,translation.src,translation.dest


        
