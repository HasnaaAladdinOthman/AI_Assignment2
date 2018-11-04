# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:05:33 2018

@author: Esraa
"""

import statsmodels.api as sm
import pandas as pd
df = pd.read_csv('train.csv', index_col=0)
df.head()
lm = sm.OLS.from_formula('medv ~ lstat', df)
result = lm.fit()
print (result.summary())