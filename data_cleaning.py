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

"""
State Field
"""

df['job_state']  = df['Location'].apply(lambda x: x.split(',')[1])
# df['job_state'].value_counts() # to see the how many jobs are there in states
# to check if jobs are in headquarters
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

"""
Age of company
"""

df['age'] = df['Founded'].apply(lambda x: x if x <1 else 2021 - x)

"""
Parsing Job Description(Python, Excel, Etc.)
"""


#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()


# droping unnamed:0 column
df_final = df.drop(['Unnamed: 0'], axis =1)


#creating new cleaned CSV
df_final.to_csv('salary_data_cleaned.csv',index = False)
















