#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:59:00 2020

@author: donghoon

converting one-hot vector to normal csv file.
"""



import pandas as pd


sample=pd.read_csv("sample_submission.csv")

result=pd.read_csv("mysubmission.csv")
result=result.drop("Unnamed: 0", axis=1)
#print(result[0:1]['0'].values[0])

print(sample[0:3]['Label'])

for i in range(len(result)):
    for j in range(10):
        if (result[i:i+1][str(j)].values[0]==1):
            #sample[i:i+1]['Label']=j
            sample.loc[i,'Label']=j
            break

print (sample)
sample.to_csv("result_answer.csv")
