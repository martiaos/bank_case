import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings #kill depreciation warningswith warnings.catch_warnings():
warnings.filterwarnings('ignore')

df = pd.read_csv('bank-full.csv', sep = ';', header=0)

data = df[['day', 'month', 'y']]

### Make dictionary of
dict = {}

for i in range(len(data)):
    m = data.iloc[i].month
    if m not in dict.keys():
        dict[m] = {}
    d = data.iloc[i].day
    if d not in dict[m].keys():
        dict[m][d] = [0,0]
    s = data.iloc[i].y
    if s == 'yes':
        dict[m][d][1] += 1
    dict[m][d][0] += 1

M = {}
for m in dict.keys():
    n = 0; s = 0;
    for d in dict[m].keys():
        n += dict[m][d][0]
        s += dict[m][d][1]
    M[m] = [s/n]

months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,\
          'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

R = [[],[]]
i = 0
for keys in M:
    R[0].append((M[keys][0]))
    R[1].append(months[keys])
    i += 1

R = np.asarray(R)
R.sort(axis=0)
plt.figure()
my_xticks = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
plt.xticks(range(1,13), my_xticks)
plt.bar(R[1,:], R[0,:])
plt.legend()
plt.xlabel('Month')
plt.ylabel('Rate of success')
plt.title('Success rate by month')
plt.savefig('success_rate_by_month.png', dpi=400)


N = []
S = []
for m in dict.keys():
    for d in dict[m].keys():
        n = dict[m][d][0]
        s = dict[m][d][1]
        N.append(n)
        S.append(s)

X = np.array([N,S])
plt.figure()
plt.scatter(X[0], X[1]/X[0], marker='x', s=.2, color='black')
plt.xlabel('Number of calls')
plt.ylabel('Rate of success')
plt.title("Success rate by number of calls per day")
plt.savefig('successrate_by_number.png', dpi=400)
