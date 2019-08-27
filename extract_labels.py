# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:07:24 2019

@author: Simon
"""

import pandas as pd
import os


def labels(path_data,subjects):
    
    for subject in subjects:
       pom=pd.read_csv(path_data+os.sep+subject+os.sep+subject+"_labels.csv")
       pom['C'] = pom['id'].diff()
       pom['C']= pom['C'].shift(-1)
       pom=pom.fillna(1)
       df_filtered = pom[pom['C'] != 0]
       df_filtered.drop(columns='C',inplace=True,axis=1)
       df_filtered.to_csv(path_data+os.sep+subject+os.sep+subject+"_corrected_labels.csv")   
       
if __name__ == "__main__":  
    
   path_data="Sliding_Window_Data"+os.sep+"Labels"
   subjects=["Subject_1","Subject_3","Subject_4", "Subject_7", "Subject_10", "Subject_11", "Subject_12", "Subject_13", "Subject_14","Subject_15","Subject_16","Subject_17"]
   labels(path_data,subjects)