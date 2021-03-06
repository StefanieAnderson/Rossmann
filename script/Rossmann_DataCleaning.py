# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 00:42:03 2015

@author: Stef
"""

# Standard Imports
import numpy as np
import pandas as pd

#Visualisation Imports
import seaborn as sns
from pylab import savefig
import matplotlib.pyplot as plt
from datetime import datetime
import datetime
import time
from sklearn import preprocessing
from pandas import Series,DataFrame
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer as DV
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV,RandomizedSearchCV
from scipy.stats import randint, uniform
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import train_test_split

# Read files and merge them
train  = pd.read_csv('../input/train.csv')
train['Date'] = pd.to_datetime(train['Date'])
train['Year'] = train['Date'].dt.year
train['Month'] = train['Date'].dt.month
train['Day'] = train['Date'].dt.day
store = pd.read_csv('../input/store.csv')
train_store = pd.DataFrame.merge(train,store,left_on='Store',right_on='Store',how='outer')

print(train.info())
print(train_store.info())