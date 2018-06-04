import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from sklearn import preprocessing
from sklearn import utils
from sklearn.metrics import scorer
from sklearn.metrics import accuracy_score


def extractBolingerFeatures(df):
    '''
    Input:
        df : A pandas DataFrame should contain adj_close , mid_band(20d), upper_bannd,'lower_band','decision'
    Output:
        x: pandas series (features_cols)
        y: pandas series (label_cols)
        npY: numpy array (label_cols)
    '''
    feature_cols = ['adj_close', '20d', 'upperband', 'lowerband']
    label_cols = ['decision']
    x = df[feature_cols]
    y = df[label_cols]
    npY = np.array(y)
    return (x, y, npY)


def ApplyModel(model, features, label, predictInputList):
     '''
    Input:
        model : a string define model u want to use (knn, dtc, gnb)
        features : A pandas DataFrame contain feature_cols will be used to train machine.
        label : A pandas DataFrame contain label_cols will be used to train machine.
        predictInputList : A list contains feature_cols u want to predict
    Output:
       A string result of the predicted input
    '''
    if str(model).lower() == 'knn'
        knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
        knn.fit(fetures, label)
        y_predict = str(knn.predict(predictList))
        return y_predict
    elif tr(model).lower() == 'dtc'
        dtc = DecisionTreeClassifier(criterion='entropy')
        dtc.fit(fetures,label)
        y_predict = str(dtc.predict(predictList))
        return y_predict
    elif str(model).lower() is 'gnb':
        gnb = GaussianNB()
        gnb.fit(fetures,label)
        y_predict = str(gnb.predict(predictList))
        return y_predict
    else : 
        print('please enter a valid knn model model')
        
