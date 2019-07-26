#import libraries necessary for this project
import numpy as np
import pandas as pd
from sklearn.model_selection import ShuffleSplit

#Import supplementary visulizations code visuals.py
import visuals as vs
#pretty display for notebooks
%matplotlib inline
#load the Boston housing dataset
data = pd.read_csv('housing.csv')
prices = data['MEDV']
features = data.drop('MEDV', axis=1)
#sucess
print("Boston housing dataset hus {} data points with {} varibales each.".format(*data.shape))
