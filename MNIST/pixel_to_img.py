#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:34:20 2020

@author: donghoon
"""

import matplotlib.pyplot as plt
import pandas as pd

file=pd.read_csv("test.csv")

img=file.loc[0].to_numpy()
#print(img)
#print(img.reshape((28,28)))


#for i in range(10):
    #img=file.loc[i].to_numpy()
plt.imshow(img.reshape((28,28)))
