# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 00:59:36 2019

@author: Simon
"""

import pandas as pd
import numpy as np
import os
import time

# visualization imports
import seaborn as sns
import matplotlib.pyplot as plt

import itertools

import scipy
from scipy.stats import randint
from scipy.stats import uniform
#from tsfresh import extract_features
from sklearn.externals import joblib

# imports for the hyperparameter searching algorithms
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

# importing functions for the metrics
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
# imports of basic classifiers and ensable classifiers
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
import xgboost as xgb



def generateSplits(test_subject):
    
    path_to_labels="Sliding_Window_Data"+os.sep+"Labels"
    path_to_features="Selected_features_Data"+os.sep+"all"+os.sep+"final_features"
    
    if test_subject=="15":
        train_subjects=["1","3","10","4"]
        test_subjects=["15"]
    elif test_subject=="16":
        train_subjects=["1","10","11","3"]
        test_subjects=["16"]
    elif test_subject=="17":
        train_subjects=["1","4","7","13"]
        test_subjects=["17"]        
        



    print("Train")

    tempXs=pd.DataFrame()
    tempLs=pd.DataFrame()

    for subject in train_subjects:
        #append subjects
        print(subject)
        path_to_subject=path_to_features+os.sep+subject+"_all_features.csv"
        dataF=pd.read_csv(path_to_subject)
        cols = dataF.columns.values
        tempXs = tempXs.append(dataF, sort=True)

        #append labels
        path_to_label=path_to_labels+os.sep+"Subject_" + subject+os.sep+"Subject_"+subject+"_corrected_labels.csv"
        dataF=pd.read_csv(path_to_label)
        tempLs = tempLs.append(dataF, sort=True)


    tempX=pd.DataFrame()

    for subject in test_subjects:
        #append subjects
        print(subject)
        path_to_subject=path_to_features+os.sep+subject+"_all_features.csv"
        dataF=pd.read_csv(path_to_subject)
        cols = dataF.columns.values
        tempX = tempX.append(dataF, sort=True)



    return tempXs,tempLs.Tag,tempLs.TimeStamps,tempX



test_subjects1=["15","16","17"]
all_predictions=pd.DataFrame()
path_to_predictions="Predictions"
for i in test_subjects1:
        
    X_train, Y_train, timestamp, X_test= generateSplits(i)
    nan_rows = X_train[X_train.isnull().T.any().T]
    print("X_train nan vrednosti:")
    print(nan_rows.shape)
    
    print("X_train nan columns")
    print(X_train.columns[X_train.isna().any()].tolist())
    
    
    
    X_train.drop(['AnkleAccelerometer x-axis__variance', 'BeltLuminosity illuminance__cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_2', 'NeckLuminosity illuminance__agg_linear_trend__f_agg_"min"__chunk_len_5__attr_"intercept"'],axis=1,inplace=True)
    #X_test.drop(['AnkleAccelerometer x-axis__variance', 'BeltLuminosity illuminance__cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_2', 'NeckLuminosity illuminance__agg_linear_trend__f_agg_"min"__chunk_len_5__attr_"intercept"'], axis=1,inplace=True)
    
    
    print("Broj na koloni")
    print(X_train.shape)
    print(X_test.shape)
    
    nan_rows = X_train[X_train.isnull().T.any().T]
    print(nan_rows.shape)
    
    #X_test = X_test[X_train.columns]
    
    
    print("Training...")
    clf=RandomForestClassifier() # use parameters obtained from parameters search script
    clf.fit(X_train, Y_train)
    
    
    
    filename = "saved_models"+os.sep+"finalized_model_" + i + ".sav"
    if not os.path.exists("saved_models"):
       os.mkdir("saved_models")
    joblib.dump(clf, filename)
    Y_predict=clf.predict(X_test)
    Y_predict['timestamp']=timestamp
    all_predictions=all_predictions.append(Y_predict)

#after all subjects are predicted, write predictions to file
    
if not os.path.exists(path_to_predictions):
    os.mkdir(path_to_predictions)
    
all_predictions.to_csv(path_to_predictions+os.sep+"predictions.csv",index=False)
    