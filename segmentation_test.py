# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:07:05 2019

@author: Simon
"""

import pandas as pd
import numpy as np
import os


def segment(subjects, path_to_data, path_to_results):
    
    for subject in subjects:
        path_to_subject=path_to_data+os.sep+subject+".csv"
        # instance counter
        id_count=0
        # the dataframe to be exported after we make the necessary concatenations, only with columns required for the feature extraction
        subject_df = pd.DataFrame(columns=["id","TimeStamps","AnkleAccelerometer x-axis","AnkleAccelerometer y-axis","AnkleAccelerometer z-axis","AnkleAccelerometerMag","AnkleAngularVelocity x-axis" ,"AnkleAngularVelocity y-axis","AnkleAngularVelocity z-axis" ,"AnkleAngularVelocityMag","AnkleLuminosity illuminance" ,"RightPocketAccelerometer x-axis","RightPocketAccelerometer y-axis" ,"RightPocketAccelerometer z-axis","RightPocketAccelerometerMag", "RightPocketAngularVelocity x-axis", "RightPocketAngularVelocity y-axis", "RightPocketAngularVelocity z-axis", "RightPocketAngularVelocityMag","RightPocketLuminosity illuminance", "BeltAccelerometer x-axis", "BeltAccelerometer y-axis", "BeltAccelerometer z-axis","BeltAccelerometerMag", "BeltAngularVelocity x-axis","BeltAngularVelocity y-axis","BeltAngularVelocity z-axis","BeltAngularVelocityMag","BeltLuminosity illuminance", "NeckAccelerometer x-axis","NeckAccelerometer y-axis","NeckAccelerometer z-axis","NeckAccelerometerMag", "NeckAngularVelocity x-axis","NeckAngularVelocity y-axis","NeckAngularVelocity z-axis","NeckAngularVelocityMag","NeckLuminosity illuminance","WristAccelerometer x-axis","WristAccelerometer y-axis","WristAccelerometer z-axis", "WristAccelerometerMag","WristAngularVelocity x-axis","WristAngularVelocity y-axis","WristAngularVelocity z-axis","WristAngularVelocityMag","WristLuminosity illuminance","BrainSensor","Trial"])
    
        temp_df=pd.read_csv(path_to_subject,header=0)
        temp_df.columns = temp_df.columns.str.strip()
    
               
        start=0
        temp_df['id']=0
      
        while start+10<temp_df.shape[0]:   #while still in the dataframe
            
            if temp_df["Trial"].iloc[start] == temp_df["Trial"].iloc[start+10]:   #no trial change
                    
                end=start+10
                new_start=start+5
                    
            else:  
                for displacement in range(1,11):
                    print(displacement)
                    if temp_df["Trial"].iloc[start+displacement] != temp_df["Trial"].iloc[start]:
                        end=start+displacement
                        new_start=end
                        break
      
            print(temp_df["Trial"].iloc[start])
            temp_df['id'].iloc[start:end]=id_count  
    
            temp_df=temp_df[["id","TimeStamps", "AnkleAccelerometer x-axis","AnkleAccelerometer y-axis","AnkleAccelerometer z-axis","AnkleAccelerometerMag","AnkleAngularVelocity x-axis" ,"AnkleAngularVelocity y-axis","AnkleAngularVelocity z-axis" ,"AnkleAngularVelocityMag","AnkleLuminosity illuminance" ,"RightPocketAccelerometer x-axis","RightPocketAccelerometer y-axis" ,"RightPocketAccelerometer z-axis","RightPocketAccelerometerMag", "RightPocketAngularVelocity x-axis", "RightPocketAngularVelocity y-axis", "RightPocketAngularVelocity z-axis", "RightPocketAngularVelocityMag","RightPocketLuminosity illuminance", "BeltAccelerometer x-axis", "BeltAccelerometer y-axis", "BeltAccelerometer z-axis","BeltAccelerometerMag", "BeltAngularVelocity x-axis","BeltAngularVelocity y-axis","BeltAngularVelocity z-axis","BeltAngularVelocityMag","BeltLuminosity illuminance", "NeckAccelerometer x-axis","NeckAccelerometer y-axis","NeckAccelerometer z-axis","NeckAccelerometerMag", "NeckAngularVelocity x-axis","NeckAngularVelocity y-axis","NeckAngularVelocity z-axis","NeckAngularVelocityMag","NeckLuminosity illuminance","WristAccelerometer x-axis","WristAccelerometer y-axis","WristAccelerometer z-axis", "WristAccelerometerMag","WristAngularVelocity x-axis","WristAngularVelocity y-axis","WristAngularVelocity z-axis","WristAngularVelocityMag","WristLuminosity illuminance","BrainSensor","Trial"]]        
            subject_df=pd.concat([subject_df,temp_df.iloc[start:end]])
            id_count+=1
            start=new_start
    
        #if there are less than 10 samples until the end of the dataframe
        temp_df['id'].iloc[start:]=id_count 
             
        subject_df=pd.concat([subject_df,temp_df.iloc[start:]]) 
             
        
        temp_path=path_to_results+os.sep+"Sensor_Data"+os.sep+subject
        if not os.path.exists(path_to_results):
            os.mkdir(path_to_results)
        if not os.path.exists(temp_path):
           os.mkdir(temp_path)
    
            
        #divide the existing dataframe into the necessery files
        subject_df[['id','AnkleAccelerometer x-axis']].to_csv(temp_path+os.sep+subject+"_AnkleAccelerometer_X.csv",index=False)
        subject_df[['id','AnkleAccelerometer y-axis']].to_csv(temp_path+os.sep+subject+"_AnkleAccelerometer_Y.csv",index=False)
        subject_df[['id','AnkleAccelerometer z-axis']].to_csv(temp_path+os.sep+subject+"_AnkleAccelerometer_Z.csv",index=False)
        subject_df[['id','AnkleAccelerometerMag']].to_csv(temp_path+os.sep+subject+"_AnkleAccelerometer_Mag.csv",index=False)
        subject_df[['id','AnkleAngularVelocity x-axis']].to_csv(temp_path+os.sep+subject+"_AnkleAngularVelocity_X.csv",index=False)
        subject_df[['id','AnkleAngularVelocity y-axis']].to_csv(temp_path+os.sep+subject+"_AnkleAngularVelocity_Y.csv",index=False)
        subject_df[['id','AnkleAngularVelocity z-axis']].to_csv(temp_path+os.sep+subject+"_AnkleAngularVelocity_Z.csv",index=False)
        subject_df[['id','AnkleAngularVelocityMag']].to_csv(temp_path+os.sep+subject+"_AnkleAngularVelocity_Mag.csv",index=False)
        subject_df[['id','AnkleLuminosity illuminance']].to_csv(temp_path+os.sep+subject+"_AnkleLuminosity_L.csv",index=False)
        subject_df[['id','RightPocketAccelerometer x-axis']].to_csv(temp_path+os.sep+subject+"_RightPocketAccelerometer_X.csv",index=False)
        subject_df[['id','RightPocketAccelerometer y-axis']].to_csv(temp_path+os.sep+subject+"_RightPocketAccelerometer_Y.csv",index=False)
        subject_df[['id','RightPocketAccelerometer z-axis']].to_csv(temp_path+os.sep+subject+"_RightPocketAccelerometer_Z.csv",index=False)
        subject_df[['id','RightPocketAccelerometerMag']].to_csv(temp_path+os.sep+subject+"_RightPocketAccelerometer_Mag.csv",index=False)
        subject_df[['id','RightPocketAngularVelocity x-axis']].to_csv(temp_path+os.sep+subject+"_RightPocketAngularVelocity_X.csv",index=False)
        subject_df[['id','RightPocketAngularVelocity y-axis']].to_csv(temp_path+os.sep+subject+"_RightPocketAngularVelocity_Y.csv",index=False)
        subject_df[['id','RightPocketAngularVelocity z-axis']].to_csv(temp_path+os.sep+subject+"_RightPocketAngularVelocity_Z.csv",index=False)
        subject_df[['id','RightPocketAngularVelocityMag']].to_csv(temp_path+os.sep+subject+"_RightPocketAngularVelocity_Mag.csv",index=False)
        subject_df[['id','RightPocketLuminosity illuminance']].to_csv(temp_path+os.sep+subject+"_RightPocketLuminosity_L.csv",index=False)
        subject_df[['id','BeltAccelerometer x-axis']].to_csv(temp_path+os.sep+subject+"_BeltAccelerometer_X.csv",index=False)
        subject_df[['id','BeltAccelerometer y-axis']].to_csv(temp_path+os.sep+subject+"_BeltAccelerometer_Y.csv",index=False)
        subject_df[['id','BeltAccelerometer z-axis']].to_csv(temp_path+os.sep+subject+"_BeltAccelerometer_Z.csv",index=False)
        subject_df[['id','BeltAccelerometerMag']].to_csv(temp_path+os.sep+subject+"_BeltAccelerometer_Mag.csv",index=False)
        subject_df[['id','BeltAngularVelocity x-axis']].to_csv(temp_path+os.sep+subject+"_BeltAngularVelocity_X.csv",index=False)
        subject_df[['id','BeltAngularVelocity y-axis']].to_csv(temp_path+os.sep+subject+"_BeltAngularVelocity_Y.csv",index=False)
        subject_df[['id','BeltAngularVelocity z-axis']].to_csv(temp_path+os.sep+subject+"_BeltAngularVelocity_Z.csv",index=False)
        subject_df[['id','BeltAngularVelocityMag']].to_csv(temp_path+os.sep+subject+"_BeltAngularVelocity_Mag.csv",index=False)
        subject_df[['id','BeltLuminosity illuminance']].to_csv(temp_path+os.sep+subject+"_BeltLuminosity_L.csv",index=False)
        subject_df[['id','NeckAccelerometer x-axis']].to_csv(temp_path+os.sep+subject+"_NeckAccelerometer_X.csv",index=False)
        subject_df[['id','NeckAccelerometer y-axis']].to_csv(temp_path+os.sep+subject+"_NeckAccelerometer_Y.csv",index=False)
        subject_df[['id','NeckAccelerometer z-axis']].to_csv(temp_path+os.sep+subject+"_NeckAccelerometer_Z.csv",index=False)
        subject_df[['id','NeckAccelerometerMag']].to_csv(temp_path+os.sep+subject+"_NeckAccelerometer_Mag.csv",index=False)
        subject_df[['id','NeckAngularVelocity x-axis']].to_csv(temp_path+os.sep+subject+"_NeckAngularVelocity_X.csv",index=False)
        subject_df[['id','NeckAngularVelocity y-axis']].to_csv(temp_path+os.sep+subject+"_NeckAngularVelocity_Y.csv",index=False)
        subject_df[['id','NeckAngularVelocity z-axis']].to_csv(temp_path+os.sep+subject+"_NeckAngularVelocity_Z.csv",index=False)
        subject_df[['id','NeckAngularVelocityMag']].to_csv(temp_path+os.sep+subject+"_NeckAngularVelocity_Mag.csv",index=False)
        subject_df[['id','NeckLuminosity illuminance']].to_csv(temp_path+os.sep+subject+"_NeckLuminosity_L.csv",index=False)
        subject_df[['id','WristAccelerometer x-axis']].to_csv(temp_path+os.sep+subject+"_WristAccelerometer_X.csv",index=False)
        subject_df[['id','WristAccelerometer y-axis']].to_csv(temp_path+os.sep+subject+"_WristAccelerometer_Y.csv",index=False)
        subject_df[['id','WristAccelerometer z-axis']].to_csv(temp_path+os.sep+subject+"_WristAccelerometer_Z.csv",index=False)
        subject_df[['id','WristAccelerometerMag']].to_csv(temp_path+os.sep+subject+"_WristAccelerometer_Mag.csv",index=False)
        subject_df[['id','WristAngularVelocity x-axis']].to_csv(temp_path+os.sep+subject+"_WristAngularVelocity_X.csv",index=False)
        subject_df[['id','WristAngularVelocity y-axis']].to_csv(temp_path+os.sep+subject+"_WristAngularVelocity_Y.csv",index=False)
        subject_df[['id','WristAngularVelocity z-axis']].to_csv(temp_path+os.sep+subject+"_WristAngularVelocity_Z.csv",index=False)
        subject_df[['id','WristAngularVelocityMag']].to_csv(temp_path+os.sep+subject+"_WristAngularVelocity_Mag.csv",index=False)
        subject_df[['id','WristLuminosity illuminance']].to_csv(temp_path+os.sep+subject+"_WristLuminosity_L.csv",index=False)
        subject_df[['id', 'BrainSensor']].to_csv(temp_path+os.sep+subject+"_BrainSensor_B.csv",index=False)
        subject_df[['id', 'TimeStamps','Tag']].to_csv(temp_path+os.sep+subject+"_labels.csv",index=False)   
        
if __name__ == "__main__":
    path_to_results="Sliding_Window_Data"
    path_to_data="Data"
    patients=[ "Subject_15", "Subject_16", "Subject_17"]
    segment(patients, path_to_data,path_to_results) 
