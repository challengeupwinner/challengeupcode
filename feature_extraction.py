# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:54:59 2019

@author: Simon
"""
import pandas as pd
import os
import 

from tsfresh import extract_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute



def extract(patients,path_data,path_result_features):
    file_trajectory=[]
    for patient in patients:
       path_to_patient=path_data+os.sep+patient
       # take only patient number in order to create a folder in path_result_features
       patient_id = str(patient).split("_")[1]
       # create a folder for the patient
       if not os.path.exists(path_result_features+os.sep+patient_id):
           os.mkdir(path_result_features+os.sep+patient_id)
       # list of data files per patient
       files = os.listdir(path_to_patient)
       for file in files:
           file_trajectory.append(path_to_patient+os.sep+file)
           curr = pd.read_csv(path_to_patient+os.sep+file)
           name_of_column=curr.columns[1]
           #curr[name_of_column]=curr[name_of_column].astype(np.float64)
           result = extract_features(curr, column_id="id", column_value=name_of_column)
           result.to_csv(path_result_features+os.sep+patient_id+os.sep+str(file).split("_")[2]+"_"+str(file).split("_")[3].split(".")[0]+"_basic_features"+".csv",index=False)

if __name__ == "__main__":
    patients=["Subject_1","Subject_3","Subject_4", "Subject_7", "Subject_10", "Subject_11", "Subject_12", "Subject_13", "Subject_14", "Subject_15", "Subject_16", "Subject_17"]
    path_data="Sliding_Window_Data"+os.sep+"Sensor_Data"
    path_result_features="Features"

    extract(patients,path_data,path_result_features)
