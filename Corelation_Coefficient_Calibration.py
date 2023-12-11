# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:26:00 2023

@author: jacob
"""

import pandas as pd

geo = pd.read_excel(r'INSERT FILEPATH FOR MIGRATION DESTINATIONS HERE')

geo_data = pd.read_excel(r'INSERT VARIABLE DATA FOR SELECT GEOGRAPHY HERE')

geo = geo.drop('Unnamed: 0', axis = 1)

geo_data = geo_data.rename({'STATE':'y2_statefips','COUNTY.1':'y2_countyfips'}, axis = 1)

geo = geo_data.merge(geo, how = 'inner')

from sklearn import linear_model 

df = geo.dropna(axis = 0)

X = df[['RACE','INCOME','TRANSPLANT','IMMIGRANT','HOME COST','RENT','DEPENDENCY','DISTANCE', 'POPULATION']]
y = df[['n2']]

regr = linear_model.LinearRegression()
regr.fit(X, y) 

y_pred = regr.predict(X)

print(regr.coef_) 

from sklearn.metrics import r2_score

print(r2_score(y, y_pred))
