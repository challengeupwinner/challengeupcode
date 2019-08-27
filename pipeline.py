# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:11:28 2019

@author: Simon
"""

import pandas as pd
import numpy as np
import os

#mport orientation_correction
import axis_rotation
import split_subjects
import magnitude_extraction
import segmentation_train
import feature_extraction
import extract_labels
import select_features_basic
import feature_vector_gen
import same_features
import feature_selection_bojana
import test_split_orientation
import segmentation_test


from tsfresh import extract_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute


axis_rotation.correction() # reads data, makes the correction and save the data - TRAIN
split_subjects.split() # reads corrected data, split each Subject in separate file, and saves it in Data directory - TRAIN

test_split_orientation.func() # THIS FUNCTION IS FOR TEST SUBJECTS

patients=["Subject_1.csv","Subject_3.csv","Subject_4.csv", "Subject_7.csv", "Subject_10.csv", "Subject_11.csv", "Subject_12.csv", "Subject_13.csv", "Subject_14.csv","Subject_15.csv","Subject_16.csv","Subject_17.csv"]
sensors=["AnkleAccelerometer", "AnkleAngularVelocity","AnkleLuminosity", "RightPocketAccelerometer", "RightPocketAngularVelocity", "RightPocketLuminosity", "BeltAccelerometer", "BeltAngularVelocity", "BeltLuminosity", "NeckAccelerometer", "NeckAngularVelocity", "NeckLuminosity", "WristAccelerometer", "WristAngularVelocity", "WristLuminosity", "BrainSensor", "Infrared1", "Infrared2", "Infrared3", "Infrared4", "Infrared5", "Infrared6"]
acc_sensors=["AnkleAccelerometer", "RightPocketAccelerometer", "BeltAccelerometer","NeckAccelerometer", "WristAccelerometer"]
gyr_sensors=["AnkleAngularVelocity", "RightPocketAngularVelocity", "BeltAngularVelocity","NeckAngularVelocity", "WristAngularVelocity"]


path_to_data="Data"
column_order=["TimeStamps","AnkleAccelerometer x-axis","AnkleAccelerometer y-axis","AnkleAccelerometer z-axis","AnkleAccelerometerMag","AnkleAngularVelocity x-axis" ,"AnkleAngularVelocity y-axis","AnkleAngularVelocity z-axis" ,"AnkleAngularVelocityMag","AnkleLuminosity illuminance" ,"RightPocketAccelerometer x-axis","RightPocketAccelerometer y-axis" ,"RightPocketAccelerometer z-axis","RightPocketAccelerometerMag", "RightPocketAngularVelocity x-axis", "RightPocketAngularVelocity y-axis", "RightPocketAngularVelocity z-axis", "RightPocketAngularVelocityMag","RightPocketLuminosity illuminance", "BeltAccelerometer x-axis", "BeltAccelerometer y-axis", "BeltAccelerometer z-axis","BeltAccelerometerMag", "BeltAngularVelocity x-axis","BeltAngularVelocity y-axis","BeltAngularVelocity z-axis","BeltAngularVelocityMag","BeltLuminosity illuminance", "NeckAccelerometer x-axis","NeckAccelerometer y-axis","NeckAccelerometer z-axis","NeckAccelerometerMag", "NeckAngularVelocity x-axis","NeckAngularVelocity y-axis","NeckAngularVelocity z-axis","NeckAngularVelocityMag","NeckLuminosity illuminance","WristAccelerometer x-axis","WristAccelerometer y-axis","WristAccelerometer z-axis", "WristAccelerometerMag","WristAngularVelocity x-axis","WristAngularVelocity y-axis","WristAngularVelocity z-axis","WristAngularVelocityMag","WristLuminosity illuminance","BrainSensor","Infrared1","Infrared2","Infrared3","Infrared4","Infrared5","Infrared6","Subject","Trial","Activity","Tag"]



#-------------Vector Magnitude Extraction -----------------------------

magnitude_extraction.mag(patients,path_to_data,acc_sensors,gyr_sensors)

#---------------Data Segmentation Train --------------------  

path_to_results="Sliding_Window_Data"

patients_train=[ "Subject_1", "Subject_3", "Subject_4", "Subject_7", "Subject_10", "Subject_11", "Subject_12", "Subject_13", "Subject_14"]

if not os.path.exists(path_to_results):
   os.mkdir(path_to_results)
   
if not os.path.exists(path_to_results+os.sep+"Sensor_Data"):
   os.mkdir(path_to_results+os.sep+"Sensor_Data")
   
if not os.path.exists(path_to_results+os.sep+"Labels"):
   os.mkdir(path_to_results+os.sep+"Labels")


segmentation_train.segment(patients, path_to_data,path_to_results)


#---------------Data Segmentation Test --------------------  


path_to_results="Sliding_Window_Data"
patients_test=["Subject_15","Subject_16","Subject_17"]


segmentation_test.segment(patients, path_to_data, path_to_results)
    


    
    
#-------------------Feature Extraction Tsfresh---------------------

patients=["Subject_1","Subject_3","Subject_4", "Subject_7", "Subject_10", "Subject_11", "Subject_12", "Subject_13", "Subject_14", "Subject_15", "Subject_16", "Subject_17"]
path_data="Sliding_Window_Data"+os.sep+"Sensor_Data"
path_result_features="Features"

if not os.path.exists(path_result_features):
   os.mkdir(path_result_features)
   
feature_extraction.extract(patients,path_data,path_result_features)

#----------------------Extract Labels --------------------

path_data="Sliding_Window_Data"+os.sep+"Labels"
subjects=["Subject_1","Subject_3","Subject_4", "Subject_7", "Subject_10", "Subject_11", "Subject_12", "Subject_13", "Subject_14"]

extract_labels.labels(path_data,subjects)
   
#-------------------Remove Unnecessary Features------------

path_result_selected_features="Selected_features_Data"
path_data="Features"
subjects=["1","3","4","7","10","11","12","13","14"]

if not os.path.exists(path_result_selected_features):
   os.mkdir(path_result_selected_features)

select_features_basic.select(path_result_selected_features,path_data,subjects)
       
       
#-----------Feature Vector Generation--------------------------


path_to_features="Selected_features_Data"
patients=["1","3","4","7","10","11","12","13","14","15","16","17"]

if "all" not in os.listdir(path_to_features):
   os.mkdir(path_to_features+os.sep+"all")

feature_vector_gen.generate(path_to_features,patients)



#
##----------------Same TSFRESH Selected Features in Each File
#
#After feature vectors are generated, we need to make sure that each subject file has the same columns
#bad implementation, might be slow

path = "Selected_features_Data" + os.sep + "all"
path_to_result = path + os.sep + "fixed_columns"

if not os.path.exists(path_to_result):
   os.mkdir(path_to_result)
   
same_features.select_same(path,path_to_result)



#-------------------All Sensors feature selection------------------
feature_selection_bojana.select_feature()

