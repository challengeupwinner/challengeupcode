# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:15:50 2019

@author: Simon
"""
# this script appends all features extracted for each sensor in one file
import pandas as pd
import os

def generate(path_to_features,patients):
    all_df=pd.DataFrame()
    first=True
    for patient in patients:
       print(patient)
       path_to_patient=path_to_features+os.sep+patient
       patient_df=pd.DataFrame()
       for dat in os.listdir(path_to_patient):
           print(dat)
           df=pd.read_csv(path_to_patient+os.sep+dat)
           patient_df=pd.concat([patient_df,df],axis=1)
       if first:
           common_columns=patient_df.columns
           all_df=patient_df
           first=False
       else:
           common_columns=patient_df.columns.intersection(all_df.columns)
           all_df=pd.concat([all_df[common_columns],patient_df[common_columns]],axis=0)
       print("Zapisano")
       patient_df[common_columns].to_csv(path_to_features+os.sep+"all"+os.sep+patient+"_all_features.csv",index=False)
    first=True
    
if __name__ == "__main__":
    
    path_to_features="Selected_features_Data"
    patients=["1","3","4","7","10","11","12","13","14","15","16","17"]
    generate(path_to_features,patients)