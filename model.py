import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings #kill depreciation warningswith warnings.catch_warnings():
warnings.filterwarnings('ignore')

df = pd.read_csv('bank-full.csv', sep = ';', header=0)

# Overview
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
sns.countplot(x='y', data=df)
plt.show()



# Data cleaning

## Create dummy variables
categories = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
for var in categories:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(df[var], prefix=var)
    df = df.join(cat_list)

## Create boolean variables
bools = ['default', 'housing', 'loan', 'y']

def boolean(df, name):
    df[name] = (df[name] == 'yes').astype(int)
    return df

for var in bools:
    df = boolean(df, var)

## Remove variables
df = df.drop(['job_unemployed','marital_single','education_primary', \
'contact_cellular', 'month_jan', 'poutcome_failure'],1)

df['intercept'] = 1

variables = (df.columns.values.tolist())
keep = [i for i in variables if i not in categories]
data = df[keep]

# Data summary
data.info()

# Descriptive statistics

print(df.groupby("y").mean())

a = 0
months = ['feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
for month in months:
    i = 'month_' + month
    a += df.groupby('y')[i].mean()
print(a)

# Regression

y = ['y']
x = [i for i in keep if i not in y]
Y = data[y]
X = data[x]

import statsmodels.api as sm

logit_model = sm.Logit(Y,X)
result = logit_model.fit()
print(result.summary2())
