# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:52:29 2019

@author: Simon
"""

import pandas as pd
import os



def split():
        
    path_data=".."+os.sep+"Data"
    
    data=pd.read_csv(".."+os.sep+"Raw_data"+os.sep+"CompleteDataSet_training_competition.csv")
    
    if not os.path.exists(path_data):
        os.mkdir(path_data)
        
        
    subjects=data['Subject'].unique()
    
    for subject in subjects:
        data1=data.loc[data['Subject']==subject]
        data1.to_csv(path_data+os.sep+"Subject_"+str(subject)+".csv",index=False)
        
if __name__ == "__main__":
    split()
