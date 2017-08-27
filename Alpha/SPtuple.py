'''
Created on 2017.8.22

@author: ZhongqiLi
'''

class SPtulpe(object):
    '''
    Subject - Predicate Tuples
    '''


    def __init__(self, predicate,subject,tweetIndex):
        '''
        Constructor
        '''
        self.subject_str = subject
        self.ptedicate_str = predicate
        self.tweetIndex = tweetIndex