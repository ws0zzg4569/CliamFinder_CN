'''
Created on 2017.8.22
@author: ZhongqiLi
'''
import numpy as np
import SETTINGS
from sklearn.metrics.pairwise import pairwise_distances


a = np.array([ [1,2,3] for i in range(3)])
print a.diagonal()

print a.diagonal()[:,None]
print a.diagonal()[:,None] + a.diagonal()
