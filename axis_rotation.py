# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:18:53 2019

@author: Simon
"""
import pandas as pd
import numpy as np
import os


def correction():
    train_path = ".."+os.sep+"Raw_data"+os.sep+"CompleteDataSet_training_competition.csv" # Raw_data/CompleteDataSet_training_competition.csv
    df_training = pd.read_csv(train_path)

    rt_y_180 = np.array([[-1,0,0]
                        ,[0,1,0]
                        ,[0,0,-1]])
    
    rt_z_180 = np.array([[-1,0,0,],
                         [0,-1,0],
                         [0,0,1]])
    
    rt_x_180 = np.array([[1,0,0]
                        ,[0,-1,0]
                        ,[0,0,-1]])
    
    
    
    
    
    
    neck_around_y=[4,12,13]
    
    for subject in neck_around_y:
        neck = [None]*3 
        neck[0] = df_training.loc[df_training['Subject'] == subject, 'NeckAccelerometer x-axis']
        neck[1] = df_training.loc[df_training['Subject'] == subject, 'NeckAccelerometer y-axis']
        neck[2] = df_training.loc[df_training['Subject'] == subject, 'NeckAccelerometer z-axis']
        all_rows=np.column_stack((neck[0],neck[1],neck[2]))
    
        y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
        
        df_training.loc[df_training['Subject'] == subject, 'NeckAccelerometer x-axis']=y180.iloc[:,0].values
        df_training.loc[df_training['Subject'] == subject, 'NeckAccelerometer y-axis']=y180.iloc[:,1].values
        df_training.loc[df_training['Subject'] == subject, 'NeckAccelerometer z-axis']=y180.iloc[:,2].values
        
        
    
    neck = [None]*3   
    neck[0] = df_training.loc[((df_training['Subject'] == 11) & (df_training['Activity']==1)), 'NeckAccelerometer x-axis']
    neck[1] = df_training.loc[((df_training['Subject'] == 11) & (df_training['Activity']==1)), 'NeckAccelerometer y-axis']
    neck[2] = df_training.loc[((df_training['Subject'] == 11) & (df_training['Activity']==1)), 'NeckAccelerometer z-axis'] 
    all_rows = np.column_stack((neck[0],neck[1],neck[2]))
    
    y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
    
    df_training.loc[((df_training['Subject'] == 11) & (df_training['Activity']==1)), 'NeckAccelerometer x-axis']=y180.iloc[:,0].values
    df_training.loc[((df_training['Subject'] == 11) & (df_training['Activity']==1)), 'NeckAccelerometer y-axis']=y180.iloc[:,1].values
    df_training.loc[((df_training['Subject'] == 11) & (df_training['Activity']==1)), 'NeckAccelerometer z-axis']=y180.iloc[:,2].values
    
    
    neck = [None]*3 
    neck[0] =df_training.loc[((df_training['Subject'] == 12) & (df_training['Activity']==4)), 'NeckAccelerometer x-axis']
    neck[1] =df_training.loc[((df_training['Subject'] == 12) & (df_training['Activity']==4)), 'NeckAccelerometer y-axis']
    neck[2] =df_training.loc[((df_training['Subject'] == 12) & (df_training['Activity']==4)), 'NeckAccelerometer z-axis']
    
    all_rows = np.column_stack((neck[0],neck[1],neck[2]))
    
    x180 = pd.DataFrame(all_rows.dot(rt_x_180[:,:3].T)[:,:3])
    df_training.loc[((df_training['Subject'] == 12) & (df_training['Activity']==4)), 'NeckAccelerometer x-axis']=x180.iloc[:,0].values
    df_training.loc[((df_training['Subject'] == 12) & (df_training['Activity']==4)), 'NeckAccelerometer y-axis']=x180.iloc[:,0].values
    df_training.loc[((df_training['Subject'] == 12) & (df_training['Activity']==4)), 'NeckAccelerometer z-axis']=x180.iloc[:,0].values
    
    
    
    
    pocket_around_y=[4,11]
    
    for subject in pocket_around_y:
        neck = [None]*3 
        neck[0] = df_training.loc[df_training['Subject'] == subject, 'RightPocketAccelerometer x-axis']
        neck[1] = df_training.loc[df_training['Subject'] == subject, 'RightPocketAccelerometer y-axis']
        neck[2] = df_training.loc[df_training['Subject'] == subject, 'RightPocketAccelerometer z-axis']
        all_rows=np.column_stack((neck[0],neck[1],neck[2]))
    
        y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
        
        df_training.loc[df_training['Subject'] == subject, 'RightPocketAccelerometer x-axis']=y180.iloc[:,0].values
        df_training.loc[df_training['Subject'] == subject, 'RightPocketAccelerometer y-axis']=y180.iloc[:,1].values
        df_training.loc[df_training['Subject'] == subject, 'RightPocketAccelerometer z-axis']=y180.iloc[:,2].values
        
        
    
    pocket_around=[[10,8],[14,2],[14,3]]
    
    for subject in pocket_around:
        neck = [None]*3 
        neck[0] = df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer x-axis']
        neck[1] = df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer y-axis']
        neck[2] = df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer z-axis']
        all_rows=np.column_stack((neck[0],neck[1],neck[2]))
        
        if subject[0]==10:
            x180 = pd.DataFrame(all_rows.dot(rt_x_180[:,:3].T)[:,:3])
            df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer x-axis']=x180.iloc[:,0].values
            df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer y-axis']=x180.iloc[:,1].values
            df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer z-axis']=x180.iloc[:,2].values
        else:
            y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
            df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer x-axis']=y180.iloc[:,0].values
            df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer y-axis']=y180.iloc[:,1].values
            df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1])), 'RightPocketAccelerometer z-axis']=y180.iloc[:,2].values
     
    
       
    
    pocket_around_y=[[10,1,1],[10,1,2]]
    for subject in pocket_around_y:
        neck = [None]*3 
        neck[0] = df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1]) & (df_training['Trial']==subject[2])), 'RightPocketAccelerometer x-axis']
        neck[1] = df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1]) & (df_training['Trial']==subject[2])), 'RightPocketAccelerometer y-axis']
        neck[2] = df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1]) & (df_training['Trial']==subject[2])), 'RightPocketAccelerometer z-axis']
        all_rows=np.column_stack((neck[0],neck[1],neck[2]))
    
        y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
        
        df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1]) & (df_training['Trial']==subject[2])), 'RightPocketAccelerometer x-axis']=y180.iloc[:,0].values
        df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1]) & (df_training['Trial']==subject[2])), 'RightPocketAccelerometer y-axis']=y180.iloc[:,1].values
        df_training.loc[((df_training['Subject'] == subject[0]) & (df_training['Activity']==subject[1]) & (df_training['Trial']==subject[2])), 'RightPocketAccelerometer z-axis']=y180.iloc[:,2].values
        
        
    
        
    neck = [None]*3 
    neck[0] = df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer x-axis']
    neck[1] = df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer y-axis']
    neck[2] = df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer z-axis']
    all_rows = np.column_stack((neck[0],neck[1],neck[2]))
    
    y180 = pd.DataFrame(all_rows.dot(rt_y_180[:,:3].T)[:,:3])
    
    df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer x-axis']=y180.iloc[:,0].values
    df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer y-axis']=y180.iloc[:,0].values
    df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer z-axis']=y180.iloc[:,0].values
    
    neck[0] = df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer x-axis']
    neck[1] = df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer y-axis']
    neck[2] = df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer z-axis']
    all_rows = np.column_stack((neck[0],neck[1],neck[2]))
    
    z180 = pd.DataFrame(all_rows.dot(rt_z_180[:,:3].T)[:,:3])
    
    df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer x-axis']=z180.iloc[:,0].values
    df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer y-axis']=z180.iloc[:,0].values
    df_training.loc[df_training['Subject']==3, 'RightPocketAccelerometer z-axis']=z180.iloc[:,0].values
    
if __name__ == "__main__":
    correction()
    
    
