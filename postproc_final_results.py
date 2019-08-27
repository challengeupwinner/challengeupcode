# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:02:52 2019

@author: Simon
"""

import pandas as pd


from collections import Counter
from sklearn.metrics import f1_score
import os 
path_to_predictions="Predictions"


def custom_resampler(array_like):
    data = Counter(array_like)
    print(data)
    print("---------")
   # print(type(array_like))
    if not array_like.empty:
        print(data.get)
        return max(array_like, key=data.get)
    else:
        return 'NaN'

test_predictions=pd.read_csv("predictions.csv")
test_predictions.columns=["TimeStamps","predicted"]# change clolumn names

test=pd.read_csv("CompleteDataSet_testing_competition_s.csv")
test=test[['TimeStamps']]
test['TimeStamps']=pd.to_datetime(test['TimeStamps'])


pom=pd.merge(test,test_predictions,how='left',on='TimeStamps')
pom1=pom.fillna(method='bfill')
pom1['TimeStamps']=pd.to_datetime(pom1['TimeStamps'])
pom1=pom1.set_index('TimeStamps')
pom1.columns=['predicted']
pom2=pom1.predicted.resample('s').apply(custom_resampler)
pom2=pom2.reset_index()
pom2=pom2.dropna()

pom2.to_csv(path_to_predictions+os.sep+"final_results.csv",index=False)






