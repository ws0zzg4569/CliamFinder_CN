'''
Created on 2017.8.18

@author: ZhongqiLi
'''
import pymongo
import SETTINGS

class dataReader(object):
    '''
    Reading data from local MongoDB, and doing some preprocessing of content.
    '''


    def __init__(self,client = SETTINGS.MONGODB_CLIENT, port = SETTINGS.MONGODB_PORT, dbname = SETTINGS.MONGODB_DBNAME):
        '''
        Constructor
        '''
        clinet = pymongo.MongoClient(client,port)
        db = clinet[dbname]
        self.Information = db["Information"]
        self.Tweets = db["Tweets"]
        self.Relationships = db["Relationships"]
        self.Tweets2016 = db["Tweets2016"]
        
    def cursor_tweet(self,keyword = None):
        if keyword != None:
            return self.Tweets.find({'Content':{'$regex':keyword}})
        return self.Tweets.find()
    
    def cursor_Information(self):
        return self.Information.find()    
    
    def cursor_relations(self):
        return self.Relationships.find()  
    
    def cursor_Tweets2016(self):
        return self.Tweets2016.find()
    

    
    