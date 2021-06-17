# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:12:14 2021

@author: kolat
"""
#%%
def problem3_1(txtfilename):
    infile = open(txtfilename)
    cr = 0
    for line in infile:
        cr = cr+ len(line)
        print(line,end="")
    print("\n\nThere are",cr,"letters in the file.")
infile.close()
        #%%