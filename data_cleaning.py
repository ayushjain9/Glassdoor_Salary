# -*- coding: utf-8 -*-
"""
Created on Tue May 18 2021

@author: ayushjain9

Salary parsing
Comapny name : Text Only
State Field
Age of company
Parsing Job Description(Python, Excel, Etc.)
"""


import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')


"""
Salary parsing
"""

#removing -1 from salary
df = df[df['Salary Estimate'] != '-1']

#Removing est

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))


df['hourly'] =  df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] =  df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in 
                                                       x.lower() else 0)


minus_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

# adding columns back to main df
df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] =(df['min_salary'] + df['max_salary'])/2

"""
Company name : Text Only
"""

# deleting the last 3 ch (rating) from compnay name. RowWise axis = 1 
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3],axis = 1)
# df = df.drop('company_txt',axis = 1)























