# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:41:22 2019

@author: Simon
"""


import pandas as pd
import numpy as np
import os

def mag(patients,path_to_data,acc_sensors,gyr_sensors):
        
    # create base path
    for subdir_name in patients:
       path_to_patient=path_to_data+os.sep+subdir_name
       df=pd.read_csv(path_to_patient, engine='python')
       for acc in acc_sensors:
           df[acc+"Mag"]=np.sqrt(np.square(df[acc+' x-axis'])+np.square(df[acc+" y-axis"])+np.square(df[acc+" z-axis"]))
           df.to_csv(path_to_patient, index=None)
       for gyr in gyr_sensors:
           df[gyr+"Mag"]=np.sqrt(np.square(df[gyr+" x-axis"])+np.square(df[gyr+" y-axis"])+np.square(df[gyr+" z-axis"]))
           df.to_csv(path_to_patient, index=None)
       df=df[["TimeStamps","AnkleAccelerometer x-axis","AnkleAccelerometer y-axis","AnkleAccelerometer z-axis","AnkleAccelerometerMag","AnkleAngularVelocity x-axis" ,"AnkleAngularVelocity y-axis","AnkleAngularVelocity z-axis" ,"AnkleAngularVelocityMag","AnkleLuminosity illuminance" ,"RightPocketAccelerometer x-axis","RightPocketAccelerometer y-axis" ,"RightPocketAccelerometer z-axis","RightPocketAccelerometerMag", "RightPocketAngularVelocity x-axis", "RightPocketAngularVelocity y-axis", "RightPocketAngularVelocity z-axis", "RightPocketAngularVelocityMag","RightPocketLuminosity illuminance", "BeltAccelerometer x-axis", "BeltAccelerometer y-axis", "BeltAccelerometer z-axis","BeltAccelerometerMag", "BeltAngularVelocity x-axis","BeltAngularVelocity y-axis","BeltAngularVelocity z-axis","BeltAngularVelocityMag","BeltLuminosity illuminance", "NeckAccelerometer x-axis","NeckAccelerometer y-axis","NeckAccelerometer z-axis","NeckAccelerometerMag", "NeckAngularVelocity x-axis","NeckAngularVelocity y-axis","NeckAngularVelocity z-axis","NeckAngularVelocityMag","NeckLuminosity illuminance","WristAccelerometer x-axis","WristAccelerometer y-axis","WristAccelerometer z-axis", "WristAccelerometerMag","WristAngularVelocity x-axis","WristAngularVelocity y-axis","WristAngularVelocity z-axis","WristAngularVelocityMag","WristLuminosity illuminance","BrainSensor","Infrared1","Infrared2","Infrared3","Infrared4","Infrared5","Infrared6","Subject","Trial","Activity","Tag"]]
       df.to_csv(path_to_patient, index=None)
       
       
       
if __name__ == "__main__":
    patients=["Subject_1.csv","Subject_3.csv","Subject_4.csv", "Subject_7.csv", "Subject_10.csv", "Subject_11.csv", "Subject_12.csv", "Subject_13.csv", "Subject_14.csv","Subject_15.csv","Subject_16.csv","Subject_17.csv"]
    acc_sensors=["AnkleAccelerometer", "RightPocketAccelerometer", "BeltAccelerometer","NeckAccelerometer", "WristAccelerometer"]
    gyr_sensors=["AnkleAngularVelocity", "RightPocketAngularVelocity", "BeltAngularVelocity","NeckAngularVelocity", "WristAngularVelocity"]
    path_to_data="../Data"
    mag(patients,path_to_data,acc_sensors,gyr_sensors) # if started from cmd, script should be upgraded to get arguments
