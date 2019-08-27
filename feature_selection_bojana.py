# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:51:40 2019

@author: Simon
"""
# Classic Imports
import itertools
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Feature Selection Imports
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

def select_feature():
    
    path_to_features="Selected_features_Data"+os.sep+"all"
    patients=["1","3","4","7","10","11","12","13","14"]
    path_to_labels="Sliding_Window_Data"+os.sep+"Labels"
    #x_train -data   y_train labels
    X_train=pd.DataFrame()
    Y_train=pd.DataFrame()
    
    for patient in patients:
        df=pd.read_csv(path_to_features+os.sep+patient+"_all_features.csv")
        X_train=X_train.append(df)
        
        path_to_label=path_to_labels+os.sep+"Subject_"+patient+os.sep+"Subject_"+patient+"_corrected_labels.csv"
        dataF=pd.read_csv(path_to_label)
        Y_train = Y_train.append(dataF, sort=True)
    
    
    X_train.dropna(axis=1, how='any',inplace=True)
    Y_train=Y_train['Tag'] 
    

    
    # Get feature names
    feature_names = list(X_train.columns.values)
    print(feature_names)

    # Calculating mutual information with the target
    # IMPORTANT NOTE: K needs to be changed to something bigger on the real data
    selector = SelectKBest(score_func=mutual_info_classif, k=1000)
    # Fitting data_frame with corresponding labels and transforming to new data (without features)
    X_train_new = selector.fit_transform(X_train, Y_train)
    
    # Get selected K best features
    new_features = []
    selector_support = selector.get_support()
    for bool, feature in zip(selector_support, feature_names):
        if bool:
            new_features.append(feature)
    print('New features: ', new_features)
    print('Old Data: ', X_train)
    print('Old Data: ', X_train[new_features])
    print('Old Data Shape', X_train.shape)
    print('New Data: ', X_train_new)
    print('New Data Shape', X_train_new.shape)
    
    # Select chosen features from train (though they already exist in X_train_new)
    X_train = X_train[new_features]
    
    
    # Separate new_features list into chunks for correlation comparison
    def chunks(l, n):
        # For item j in a range that is a length of l,
        for j in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[j:j+n]
    
    chunks_mi = list(chunks(new_features, 5))
    print(chunks_mi)
    
    # Choose feature based on Pearson correlation coefficient
    correlation_features = []
    for k in range(len(chunks_mi)):
        current_features = []
        redundant_features = []
        for chosen_feature in correlation_features:
            current_features.append(chosen_feature)
        for chunk in chunks_mi[k]:
            current_features.append(chunk)
        for a, b in itertools.combinations(current_features, 2):
            if X_train[a].corr(X_train[b]) > 0.8:
                if b not in redundant_features:
                    redundant_features.append(b)
        # print('Redundant features: ', redundant_features)
        for feature in redundant_features:
            current_features.remove(feature)
        correlation_features = current_features
    print('Final features (after correlation): ', correlation_features)
    
    # Select columns with low correlation coefficient from a data
    # print(X_train)
    # print(X_train[correlation_features])
    X_train = X_train[correlation_features]
    
    wrapper_features = []
    wrapper_features_f1 = []
    previous_accuracy = 0
    previous_accuracy_f1 = 0
    for correlation_feature in correlation_features:
        wrapper_features.append(correlation_feature)
        wrapper_features_f1.append(correlation_feature)
        no_wrapper_features = len(wrapper_features)
        no_wrapper_features_f1 = len(wrapper_features_f1)
        X_train_wrapper = X_train[wrapper_features]
        X_train_wrapper_f1 = X_train[wrapper_features_f1]
        X_test_wrapper = X_train[wrapper_features]
        X_test_wrapper_f1 = X_train[wrapper_features_f1]
        clf_important = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)
        clf_important_f1 = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)
        clf_important.fit(X_train_wrapper.values.reshape(-1, no_wrapper_features), Y_train.values.reshape(-1, 1))
        clf_important_f1.fit(X_train_wrapper_f1.values.reshape(-1, no_wrapper_features_f1), Y_train.values.reshape(-1, 1))
        y_pred = clf_important.predict(X_test_wrapper)
        y_pred_f1 = clf_important.predict(X_test_wrapper_f1)
        accuracy = accuracy_score(Y_train, y_pred)
        accuracy_f1 = f1_score(Y_train, y_pred_f1, average='macro')
    
        print("Wrapper features in each iteration: ", wrapper_features)
        print("Wrapper features in each iteration: ", wrapper_features_f1)
        print("Accuracy, Previous Accuracy: ", accuracy, previous_accuracy)
        print("Accuracy, Previous Accuracy: ", accuracy_f1, previous_accuracy_f1)
    
        if (previous_accuracy - accuracy) > 0.01:
            del wrapper_features[-1]
        else:
            previous_accuracy = accuracy
        if (previous_accuracy_f1 - accuracy_f1) > 0.01:
            del wrapper_features_f1[-1]
        else:
            previous_accuracy_f1 = accuracy_f1
    
    
    if not os.path.exists("feature_selection"):
       os.mkdir("feature_selection")
       
    file = open("feature_selection"+os.sep+"wrapper_features_f1.txt",'w') 
    for feature in wrapper_features_f1:
        file.write(feature+"\n")
    
    file.close() 
    
    file = open("feature_selection"+os.sep+"wrapper_features.txt",'w') 
    for feature in wrapper_features_f1:
        file.write(feature+"\n")
    
    file.close() 
    
    
    del X_train, Y_train
    
#--------------The following code is used to write the feature vectors only with columns selected in the feature selection process
    
    file = open("feature_selection"+os.sep+"wrapper_features_f1.txt","r")
    a = file.read()
    wrapper_features_f1 = a.split('\n')
    wrapper_features_f1=wrapper_features_f1[:-1]
    
    wrapper_features_f1.remove('BeltLuminosity illuminance__cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_2')
    wrapper_features_f1.remove('NeckLuminosity illuminance__agg_linear_trend__f_agg_"min"__chunk_len_5__attr_"intercept"')
    wrapper_features_f1.remove('AnkleAccelerometer x-axis__variance')

    path_to_features="Selected_features_Data"+os.sep+"all"
    patients=os.listdir(path_to_features+os.sep+"fixed_columns")
    
    print(patients)    
    
    if not os.path.exists(path_to_features+os.sep+"final_features"):
       os.mkdir(path_to_features+os.sep+"final_features")
    
    for patient in patients:


        df=pd.read_csv(path_to_features+os.sep+"fixed_columns"+os.sep+patient)
        df=df[wrapper_features_f1]
        df.to_csv(path_to_features+os.sep+"final_features"+os.sep+patient,index=False)
    
    


if __name__ == '__main__':
    select_feature()













    
    
    

