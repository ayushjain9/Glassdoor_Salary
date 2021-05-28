# -*- coding: utf-8 -*-
"""
Created on Fri May 28 

@author: ayushjain9


# Choose Relevant columns " Type of data cleaning"
# Get dummy variable . "Every categorical col should have each col"
                        "One hot encoder can also be used"
# train test split "train validate and test"
# multiple linear regression
# lasso regression "WHY??"
# random forest
# tune model usiing GridSearchCV
# test ensembles


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
















