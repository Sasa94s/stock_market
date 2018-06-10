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
from decimal import Decimal


def backtest_bollinger(data):
    
    signals = data
    signals["20d"] = np.round(signals["close"].rolling(window = 20, center = False).mean(), 2)

    # 2. Compute rolling standard deviation
    apple_rstd = np.round(signals['close'].rolling(window = 20, center = False).std(), 2)

    # 3. Compute upper and lower bands
    signals['upperband'] = signals['20d'] + 2 * apple_rstd
    signals['lowerband'] = signals['20d'] - 2 * apple_rstd

    # Check if the high and low get through upperband and lowerband
    signals['high-upperband'] = signals['high'].astype(float) - signals['upperband'].astype(float)
    signals['low-lowerband'] = signals['low'].astype(float)-signals['lowerband'].astype(float)

    # Label
    signals['decision'] = np.where(signals['high-upperband'] > 0.0 , 'Sell',np.where( signals['low-lowerband'] < 0.0,'Buy','Buy & Sell'))
    signals = signals.dropna()

    features_col = ['high','low','upperband','lowerband']
    label_col = ['decision']
    features = signals[features_col]
    label = signals[label_col]
    
    return (features,label)


def ApplyModel(model, features, label, predictInputList):

    if str(model).lower() == 'knn':
        knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
        knn.fit(features, label)
        y_predict = str(knn.predict(predictInputList))
        return y_predict

    elif str(model).lower() == 'dtc':
        dtc = DecisionTreeClassifier(criterion='entropy')
        dtc.fit(fetures, label)
        y_predict = str(dtc.predict(predictList))
        return y_predict

    elif str(model).lower() == 'gnb':
        gnb = GaussianNB()
        gnb.fit(fetures, label)
        y_predict = str(gnb.predict(predictList))
        return y_predict
