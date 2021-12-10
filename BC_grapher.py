#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 23:38:55 2021

@author: meg
"""
import lbf
import lb
import sem
import cp
def main(): #identify what type of graph is desired
    loc = input('Where would you like the graph to be saved? \n File Path: ') + '/'
    graph = input("What kind of graph would you like to make? \n Linear Line of Best Fit: lbf \n Lineweaver-Burk: lb \n Points with SEM bars: sem \n Connected Points: cp \n Enter the key letters: "  )
    if graph == 'lbf':   # call that graph's function
        lbf.lbf(loc)
    elif graph == 'lb':
        # Lineweaver-Burk is a double reciprical plot, but if the recipricals have already
        # been taken, it is essentially just a lbf plot
        inv = input('Has the data already been processed as its inverses?: (y/n) ')
        if inv == 'y':
            lbf.lbf(loc)
        else:
            lb.lb(loc)
    elif graph == 'sem':
        sem.sem(loc)
    elif graph == 'cp':
        cp.cp(loc)
    #elif graph == 
    else:
       print('You have not selected a valid graph type. Try again.')
while True:
    main()
    repeat = input('If you would like to make another graph, type y to continue, type anything else to exit: ')
    if repeat == 'y':
        pass
    else:
        break
