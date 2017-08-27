'''
Created on 2017.8.27
@author: ZhongqiLi
'''
from pyclausie import ClausIE
cl = ClausIE.get_instance(jar_filename='./clausie/clausie.jar')
for i in range(1):
    S = ['I learned that the 2012 Sasquatch music festival is scheduled for May 25th until May 28.']
    triples = cl.extract_triples(S)
    for t in triples:
        print t 