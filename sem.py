#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import data_sem as data
import matplotlib.pyplot as plot
def sem(loc):
    x,nAbs,eAbs = data.data_sem()
    tit = input('Input the graph title: ')
    fn = input('Input the file name: ')
    xtit = input('Input the x-axis title: ')
    ytit = input('Input the y-axis title: ')
    
    #plots the mean data points and their sem bars
    plot.errorbar(x, nAbs, yerr=eAbs, color = 'k', fmt='r.')
    plot.title(tit)
    plot.xlabel(xtit)
    plot.ylabel(ytit)
    
# Save the figure and show
    plot.tight_layout()
    plot.savefig(loc + fn + ".png")
    plot.show()
    