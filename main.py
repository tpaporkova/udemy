'''
this program charts the 10 cheapest and 10 most popular courses
'''

# pylint C:\Users\Татьяна\python\зачёт\udemy.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t = pd.read_csv('udemy_courses.csv')

t = t.sort_values(by='price').reset_index(drop=True)
i = 0
while t['price'][i] == 0:
    i += 1                             # last unpaid course index

paid = t[i:].reset_index(drop=True)    # only paid courses
cheap = paid[:10]                      # 10 cheapest courses
x = np.arange(1, 11)
plt.bar(x, cheap['price'])
plt.show()

sort_popular = paid.sort_values(by='num_subscribers', ascending=False).reset_index(drop=True)
popular = sort_popular[:10]            # 10 most popular courses
x = np.arange(1, 11)
plt.bar(x, popular['num_subscribers'])
plt.show()

# comment for git
