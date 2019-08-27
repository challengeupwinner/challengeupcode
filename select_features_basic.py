# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:11:01 2019

@author: Simon
"""
import pandas as pd
import os
from tsfresh import extract_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute

def select(path_result_selected_features,path_data,subjects):
        
    for subject in subjects:
       senzori=os.listdir(path_data+os.sep+str(subject))
       if not os.path.exists(path_result_selected_features+os.sep+str(subject)):
           os.mkdir(path_result_selected_features+os.sep+str(subject))
       for senzor in senzori:
           extracted_features=pd.read_csv(path_data+os.sep+str(subject)+os.sep+senzor)
           impute(extracted_features)
           pom=pd.read_csv("Sliding_Window_Data"+os.sep+"Labels"+os.sep+"Subject_"+str(subject)+os.sep+"Subject_"+str(subject)+"_corrected_labels.csv")
           y=pom['Tag']
           features_filtered = select_features(extracted_features, y)
           features_filtered.to_csv(path_result_selected_features+os.sep+str(subject)+os.sep+senzor.split(".")[0]+"_SELECTED.csv",index=False)
          

if __name__ == "__main__":

    path_result_selected_features="Selected_features_Data"
    path_data="Features"
    subjects=["1","3","4","7","10","11","12","13","14","15","16","17"]
    select(path_result_selected_features,path_data,subjects)
