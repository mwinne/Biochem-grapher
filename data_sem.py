#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
def data_sem():
    path = input("Copy and paste the file path for the .xlsx file with the data: ")
    df = pd.read_excel (path)  #converts the excel file into a pandas dataframe
    for cf in df.columns:   #lists out the titles of the dataframe columns
        print(cf)
    x_title = input('What column has your x-axis data? (Paste from list above): ')
    x = df[x_title].values
    new_df = df.drop(columns = [x_title]) #removes x-axis data
     
    #creates a tuple of the replicate data points
    Abs = [(new_df.iloc[i,0], new_df.iloc[i,1]) for i in range(new_df.shape[0])]
    #takes the mean of the data points in each pair
    nAbs = [np.mean(Abs[i]) for i in range(new_df.shape[0])]
    #calculates the standard error of the mean for the replicate data points
    eAbs = [(np.std(Abs[i], ddof=1) / np.sqrt(np.size(Abs[i:]))) for i in range(new_df.shape[0])]
    return x, nAbs, eAbs
