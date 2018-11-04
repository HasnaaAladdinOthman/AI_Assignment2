# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 00:15:56 2018

@author: Esraa
"""

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('train.csv')

lstat=data.lstat
medv=data.medv

x_mean= sum(lstat,1)/333
y_mean= sum(medv,1)/333

#lstate
B1= sum((lstat-x_mean)*(medv-y_mean),1)/sum((lstat-x_mean)**2,1)
B0=y_mean-(B1*x_mean)

print(B0)
print(B1)