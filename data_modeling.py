# -*- coding: utf-8 -*-
"""
Created on Fri May 28 

@author: ayushjain9


# Choose Relevant columns " Type of data cleaning"
# Get dummy variable . "Every categorical col should have each col"
                        "One hot encoder can also be used"
# train test split "train validate and test"
# multiple linear regression
# lasso regression "type of linear regression which helps to reduce overfitting"
# random forest
# tune model usiing GridSearchCV
# test ensembles

Result Random forest gives the best model least error

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('salary_data_eda.csv')

# Choose relevant Columns
df.columns

df_model = df[['avg_salary','Rating','Size','Type of ownership',
               'Industry','Sector','Revenue','num_comp','hourly',
               'employer_provided', 'job_state','same_state',
               'age','python_yn','spark','aws','excel','job_simp',
               'seniority','desc_len']]


# Get dummy variable . Every categorical col should have each col
df_dum = pd.get_dummies(df_model)
#Before splitting we can use get_dummies but bes practice is to use One hot encoder


# train test split

from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis =1)
#y = df_dum.avg_salary
y = df_dum.avg_salary.values # array is recommended. that's why "values"

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)



# multiple linear regression
# stats ols model is used for analysing

import statsmodels.api as sm

X_sm = X = sm.add_constant(X) # add a constant for X df

model = sm.OLS(y,X_sm) # building model
model.fit().summary() # fitting model

# p< 0.05 is relevant column
# Result : Too much of multi-collinearity so can'tt judge on particular to this model
# 70 % accuracy


# lasso regression
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)

# cross validation will run sample and vaildation set. Mini test
from sklearn.model_selection import cross_val_score
cross_val_score(lm,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 2)

# on avg we are off by 20000$
np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))


# lasso regression

from sklearn.linear_model import Lasso

lm_l = Lasso()
np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))
lm_l.fit(X_train, y_train)
# it gave worse then the previous

# Lets check with random forest
# random forest

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()


np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3))
# """ giving 15 """ # Tuning needed

rf.fit(X_train, y_train)


# tune models GridsearchCV 
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)


gs.best_score_
# 14.8

gs.best_estimator_
# to check the parametres
# RandomForestRegressor(n_estimators=210)

rf = RandomForestRegressor(n_estimators=210)
rf.fit(X_train, y_train)

# Boosted regressor

from sklearn.ensemble import GradientBoostingRegressor

clf=GradientBoostingRegressor(n_estimators=80,random_state=400)
clf.fit(X_train,y_train)


clf.score(X_test,y_test)


# Test ensembles 
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)
tpred_br = clf.predict(X_test)


from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)            # error 258384

mean_absolute_error(y_test,tpred_lml)           # 23

mean_absolute_error(y_test,tpred_rf)            # 11

mean_absolute_error(y_test,tpred_br)            # 16


# random forest giving the least error

mean_absolute_error(y_test,(tpred_lm+tpred_rf)/2)

import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
# with open(file_name, 'rb') as pickled:
#    data = pickle.load(pickled)
 #   model = data['model']

# model.predict(np.array(list(X_test.iloc[1,:])).reshape(1,-1))[0]

# list(X_test.iloc[1,:])
