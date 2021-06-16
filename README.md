# Glassdoor_Salary
Repo for the data science Salary prediction . End to End implementation

# Project Overview
1. Tool that estimates the data science salary.
2. Feature Engineering : Quatify the job Text description that company provides segretated to Python, Excel, AWS, and Spark columns.
3. Optimized Linear, Lasso and RandomForest and Gradient Boost Regressors using GridSearchCV to reach best model.
4. Bulit a client facing API using flask.

# Code and Resources Used/ References
**Python Version:** 3.7
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
**For Web Framework Requirements:** pip install -r requirements.txt
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

# DataSet
*  1000 job postings from glassdoor.com.
*  Job title
Salary Estimate
Job Description
Rating
Company
Location
Company Headquarters
Company Size
Company Founded Date
Type of Ownership
Industry
Sector
Revenue
Competitor

PS: Scrapping didn't worked for Glassdoor India and Glassdoor UK/USA due to Location. So team downloaded the data from Kaggle

# Data Cleaning

Parsed numeric data out of salary
Made columns for employer provided salary and hourly wages
Removed rows without salary
Parsed rating out of company text
Made a new column for company state
Added a column for if the job was at the company’s headquarters
Transformed founded date into age of company
Made columns for if different skills were listed in the job description:
Python
R
Excel
AWS
Spark
Column for simplified job title and Seniority
Column for description length

# EDA
Distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.
![image](https://user-images.githubusercontent.com/52231226/122258605-d7068880-ceee-11eb-9513-fb2129c7469f.png)
![image](https://user-images.githubusercontent.com/52231226/122258620-dcfc6980-ceee-11eb-89db-b56f993e2858.png)
![image](https://user-images.githubusercontent.com/52231226/122258639-e38ae100-ceee-11eb-965f-c6a80e972a2b.png)

# Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:

Multiple Linear Regression – Baseline for the model
Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

# Model Performance
The Random Forest model far outperformed the other approaches on the test and validation sets.

Random Forest : MAE = 11.22
Linear Regression: MAE = 18.86
Ridge Regression: MAE = 19.67

# Productionized
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.


# References:
## Used Raw CSV from the github given :
Scrapping the data from glass door using selenium (Used USA Glasdoor URL Because IN Url was not giving permission to extract data)
@url: https://github.com/arapfaik/scraping-glassdoor-selenium


## OneHotEncoder() vs pandas.get_dummies
@url: https://albertum.medium.com/preprocessing-onehotencoder-vs-pandas-get-dummies-3de1f3d77dcc
