'''
Created on 2017.8.22

@author: ZhongqiLi
'''
import numpy as np
import SETTINGS
import pickle
from SPtuple import SPtulpe

# model_Spectral = SpectralClustering()
# model_Kmeans = KMeans()

spts = pickle.load(open('./SPtuples','rb'))
print len(spts)
print  'Loaded!'

