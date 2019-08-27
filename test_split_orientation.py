# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 20:16:55 2019

@author: Simon
"""


import pandas as pd
import numpy as np
import os

    
def func():
    #--------------Indentify different subjects within the whole test set----------------
    rt_x_180 = np.array([[1,0,0]
                        ,[0,-1,0]
                        ,[0,0,-1]])
    rt_y_180 = np.array([[-1,0,0]
                        ,[0,1,0]
                        ,[0,0,-1]])
    rt_z_180 = np.array([[-1,0,0,],
                         [0,-1,0],
                         [0,0,1]])#used later for axis rotation

    test_df = pd.read_csv("Raw_data"+os.sep+"CompleteDataSet_testing_competition_s.csv", low_memory=False)   
    #Change the naming of the columns (same as in the train set)
    test_df = test_df.drop(test_df.index[0])
    test_df.columns = ['TimeStamps', 'AnkleAccelerometer x-axis', 'AnkleAccelerometer y-axis', 'AnkleAccelerometer z-axis', 'AnkleAngularVelocity x-axis ', 'AnkleAngularVelocity y-axis ', 'AnkleAngularVelocity z-axis ', 'AnkleLuminosity illuminance ', 'RightPocketAccelerometer x-axis', 'RightPocketAccelerometer y-axis', 'RightPocketAccelerometer z-axis', 'RightPocketAngularVelocity x-axis', 'RightPocketAngularVelocity y-axis', 'RightPocketAngularVelocity z-axis', 'RightPocketLuminosity illuminance', 'BeltAccelerometer x-axis', 'BeltAccelerometer y-axis', 'BeltAccelerometer z-axis', 'BeltAngularVelocity x-axis', 'BeltAngularVelocity y-axis', 'BeltAngularVelocity z-axis', 'BeltLuminosity illuminance', 'NeckAccelerometer x-axis', 'NeckAccelerometer y-axis', 'NeckAccelerometer z-axis', 'NeckAngularVelocity x-axis', 'NeckAngularVelocity y-axis', 'NeckAngularVelocity z-axis', 'NeckLuminosity illuminance', 'WristAccelerometer x-axis', 'WristAccelerometer y-axis', 'WristAccelerometer z-axis', 'WristAngularVelocity x-axis', 'WristAngularVelocity y-axis', 'WristAngularVelocity z-axis', 'WristLuminosity illuminance', 'BrainSensor', 'Infrared1', 'Infrared2', 'Infrared3', 'Infrared4', 'Infrared5', 'Infrared6']
    test_df.TimeStamps = pd.to_datetime(test_df.TimeStamps)
    test_df['diffs'] = test_df.TimeStamps.transform(pd.Series.diff)    
    #Check if the timestamp difference is larger than 30 minutes => new Subject
    test_df['Subject'] = 0
    test_df.loc[test_df.diffs > '0 days 00:30:00', 'Subject'] = 1    
    test_df.reset_index(drop=True, inplace=True)
    b=test_df.index[test_df['Subject'] == 1].tolist()    
    test_df.ix[0,-1] = 15
    
    count = 16
    for i in b:
        test_df.ix[i, -1] = count
        count = count+1
    
    test_df['Subject'] = test_df['Subject'].replace({0:np.nan})
    test_df = test_df.fillna(method='ffill')        
    test_df.drop("diffs", inplace=True, axis=1)
        
        
    #------------------Split the whole dataset into different Subject_dataframes-----------------
    test_df.columns = test_df.columns.str.strip()    
    if not os.path.exists("Data"):
       os.mkdir("Data")    
    test_subjects = ["15","16","17"]     
    for subject in test_subjects:
       temp = test_df.loc[test_df.Subject == subject]
       temp.to_csv("Data"+os.sep+"Subject_" + str(subject) + ".csv", index=False)
       
    
    #----------------Change some of the orientations of the neck sensor axes and the pocket sensor axes for test subjects --------------------------------
    path_to_data="Data"
    subjects=["Subject_15","Subject_16","Subject_17"]
    
    for subject in subjects:
        a = pd.read_csv(path_to_data + os.sep + subject + ".csv")
    
        if subject == "Subject_15":
            lista=[['NeckAccelerometer x-axis','NeckAccelerometer y-axis','NeckAccelerometer z-axis'],['RightPocketAccelerometer x-axis','RightPocketAccelerometer y-axis','RightPocketAccelerometer z-axis']]
            for element in lista:
                neck = [None]*3  
                neck[0] = a.loc[a['Subject'] == 15, element[0]]
                neck[1] = a.loc[a['Subject'] == 15, element[1]]
                neck[2] = a.loc[a['Subject'] == 15, element[2]]
                all_rows=np.column_stack((neck[0],neck[1],neck[2]))
                y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
                a.loc[a['Subject'] == 15, element[0]]=y180.iloc[:,0].values
                a.loc[a['Subject'] == 15, element[1]]=y180.iloc[:,1].values
                a.loc[a['Subject'] == 15, element[2]]=y180.iloc[:,2].values
                
            
        if subject == "Subject_16":
            neck = [None]*3  
            neck[0] = a.loc[a['Subject'] == 16,'NeckAccelerometer x-axis']
            neck[1] = a.loc[a['Subject'] == 16,'NeckAccelerometer y-axis']
            neck[2] = a.loc[a['Subject'] == 16,'NeckAccelerometer z-axis']
            all_rows=np.column_stack((neck[0],neck[1],neck[2]))
            y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
            a.loc[a['Subject'] == 16, 'NeckAccelerometer x-axis']=y180.iloc[:,0].values
            a.loc[a['Subject'] == 16, 'NeckAccelerometer y-axis']=y180.iloc[:,1].values
            a.loc[a['Subject'] == 16, 'NeckAccelerometer z-axis']=y180.iloc[:,2].values      
            
            neck[0] = a.loc[a['Subject'] == 16,'RightPocketAccelerometer x-axis']
            neck[1] = a.loc[a['Subject'] == 16,'RightPocketAccelerometer y-axis']
            neck[2] = a.loc[a['Subject'] == 16,'RightPocketAccelerometer z-axis']
            all_rows=np.column_stack((neck[0],neck[1],neck[2]))
            x180 = pd.DataFrame(all_rows.dot(rt_x_180[:,:3].T)[:,:3])
            a.loc[a['Subject'] == 16, 'RightPocketAccelerometer x-axis']=x180.iloc[:,0].values
            a.loc[a['Subject'] == 16, 'RightPocketAccelerometer y-axis']=x180.iloc[:,1].values
            a.loc[a['Subject'] == 16, 'RightPocketAccelerometer z-axis']=x180.iloc[:,2].values 
            

            
        if subject == "Subject_17":
            neck = [None]*3  
            neck[0] = a.loc[a['Subject'] == 17,'NeckAccelerometer x-axis']
            neck[1] = a.loc[a['Subject'] == 17,'NeckAccelerometer y-axis']
            neck[2] = a.loc[a['Subject'] == 17,'NeckAccelerometer z-axis']
            all_rows=np.column_stack((neck[0],neck[1],neck[2]))
            z180 = pd.DataFrame(all_rows.dot(rt_z_180[:,:3].T)[:,:3])
            a.loc[a['Subject'] == 17, 'NeckAccelerometer x-axis']=z180.iloc[:,0].values
            a.loc[a['Subject'] == 17, 'NeckAccelerometer y-axis']=z180.iloc[:,1].values
            a.loc[a['Subject'] == 17, 'NeckAccelerometer z-axis']=z180.iloc[:,2].values      
  

       
            neck = [None]*3 
            neck[0] = a.loc[a['Subject']==17, 'RightPocketAccelerometer x-axis']
            neck[1] = a.loc[a['Subject']==17, 'RightPocketAccelerometer y-axis']
            neck[2] = a.loc[a['Subject']==17, 'RightPocketAccelerometer z-axis']
            all_rows = np.column_stack((neck[0],neck[1],neck[2]))
            
            y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
            
            a.loc[a['Subject']==17, 'RightPocketAccelerometer x-axis']=y180.iloc[:,0].values
            a.loc[a['Subject']==17, 'RightPocketAccelerometer y-axis']=y180.iloc[:,0].values
            a.loc[a['Subject']==17, 'RightPocketAccelerometer z-axis']=y180.iloc[:,0].values
            
            neck[0] = a.loc[a['Subject']==17, 'RightPocketAccelerometer x-axis']
            neck[1] = a.loc[a['Subject']==17, 'RightPocketAccelerometer y-axis']
            neck[2] = a.loc[a['Subject']==17, 'RightPocketAccelerometer z-axis']
            all_rows = np.column_stack((neck[0],neck[1],neck[2]))
            
            z180 = pd.DataFrame(all_rows.dot(rt_z_180[:,:3].T)[:,:3])
            
            a.loc[a['Subject']==17, 'RightPocketAccelerometer x-axis']=z180.iloc[:,0].values
            a.loc[a['Subject']==17, 'RightPocketAccelerometer y-axis']=z180.iloc[:,0].values
            a.loc[a['Subject']==17, 'RightPocketAccelerometer z-axis']=z180.iloc[:,0].values
            
            
        a.to_csv("Data"+os.sep + str(subject) + ".csv", index=False)
           
    #------------------Find different trials within the Subject_dataframes-------------------   
       
    path_to_data="Data"
    subjects=["Subject_15", "Subject_16","Subject_17"]
    
    for subject in subjects:
        a = pd.read_csv(path_to_data + os.sep + subject + ".csv")
    
        a.TimeStamps = pd.to_datetime(a.TimeStamps)
        a['diffs'] = a.TimeStamps.transform(pd.Series.diff)
    
        #Check if the timestamp difference if larger than 1 second => different trial
        a['Trial'] = 0
        a.loc[a.diffs > '0 days 00:00:01', 'Trial'] = 1
    
        a.reset_index(drop=True, inplace=True)
        b=a.index[a['Trial'] == 1].tolist()
    
        count = 1
        for i in b:
            a.ix[i, -1] = count
            count = count+1
    
        a['Trial'].iloc[b[0]:] = a['Trial'].iloc[b[0]:].replace({0:np.nan})
        a = a.fillna(method='ffill')
        
        a.drop("diffs", inplace=True, axis=1)
        
        a.to_csv(path_to_data + os.sep + subject + ".csv", index=False)
        
if __name__ == "__main__":
    func()