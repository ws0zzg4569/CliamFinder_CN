'''
Created on 2017.8.25

@author: ZhongqiLi
'''
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import SETTINGS


def genrateWordCloud_En(str):
    wordcloud = WordCloud(collocations=False,font_path=SETTINGS.Font_pth,width = 1400,height=1400).generate(str)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")    
    plt.show()
    
def genrateWordCloud_Cn(str):
    wordcloud = WordCloud(collocations=False,font_path=SETTINGS.Font_pth,width = 1400,height=1400).generate(unicode(str, encoding='utf8'))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")    
    plt.show()