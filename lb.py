#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
def lb(loc):
    path = input("Copy and paste the file path for the .xlsx file with the data: ")
    df0 = pd.read_excel (path)   #converts the excel file into a pandas dataframe
    for cf in df0.columns:      #lists out the titles of the dataframe columns
        print(cf)
    x_title = input('What column has your x-axis data? (Paste from list above): ')
    #remove any row with 0 that would cause an error in inversion
    df = df0[df0[x_title] != 0]
    x = df[x_title].values
    inv_x = [(x[i])**-1 for i in range(len(x))]
    new_df = df.drop(columns = [x_title]) #removes x-axis data
    
    proc = input('Is your y-axis data in absorbance or velocity? (a/v): ')
    if proc == 'a':
        #converts absorbance to velocity and then 1/velocity for each value in the replicate data points
        inv_Abs = [((((new_df.iloc[i,0]+0.05381)/0.01843/5)**-1), (((new_df.iloc[i,1]+0.05381)/0.01843/5)**-1)) for i in range(new_df.shape[0])]
    elif proc == 'v':
        #converts velocity to 1/velocity
        inv_Abs = [(((new_df.iloc[i,0])**-1), ((new_df.iloc[i,1])**-1)) for i in range(new_df.shape[0])]
    else:
        print('Try again')
        print(quit)
        quit()
    #takes the mean of the data points in each pair
    inv_nAbs = [np.mean(inv_Abs[i]) for i in range(new_df.shape[0])]
    #calculates the standard error of the mean for the replicate data points
    eAbs = [(np.std(inv_Abs[i], ddof=1) / np.sqrt(np.size(inv_Abs[i:]))) for i in range(new_df.shape[0])]
    
    tit = input('Input the graph title: ')
    fn = input('Input the file name: ')
    xtit = input('Input the x-axis title: ')
    ytit = input('Input the y-axis title: ')
    
    # plots the mean data adn their sem error bars
    plot.errorbar(inv_x, inv_nAbs, yerr=eAbs, color = 'k', fmt='r.')
    # generates line of best fit
    m, b = np.polyfit(inv_x, inv_nAbs, 1)
    plot.plot(inv_x, m*x +b, color = 'k')
    plot.title(tit)
    plot.xlabel(xtit)
    plot.ylabel(ytit)
# Save the figure and show
    plot.tight_layout()
    # concatenates the strings to save the file in the desired spot
    plot.savefig(loc + fn + ".png")
    plot.show()