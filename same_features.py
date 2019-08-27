# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:48:02 2019

@author: Simon
"""
import pandas as pd
import os

def select_same(path,path_to_result):
        
    all_files = os.listdir(path)
    columns = {}
    for af in all_files:
       a = pd.read_csv(path + os.sep + af)
       columns[af] = a.shape[1]
    
    basic = min(columns, key = lambda x: columns.get(x) )
    min_col = columns[basic]
    column_file = pd.read_csv(path + os.sep + basic)
    all_columns = column_file.columns
    
    
    for af in all_files:
       df_b = pd.read_csv(path + os.sep + af)
       file_columns = df_b.columns.values
       for fc in file_columns:
           if fc not in all_columns:
               df_b = df_b.drop(fc,axis=1)
       print("Finished " + af)
       print(df_b.shape)
       df_b.to_csv(path_to_result + os.sep + af.split(".")[0] + "_fixed_columns.csv" , index=False)

if __name__ == "__main__":
    path = "Selected_features_Data" + os.sep + "all"
    path_to_result = path + os.sep + "fixed_columns"
    select_same(path,path_to_result)
