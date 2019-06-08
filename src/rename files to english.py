# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 12:49:21 2019

@author: jaide
"""

import os
import tkinter as tk
from tkinter.filedialog import askdirectory


if __name__=="__main__":
    
    root = tk.Tk()
    parent_directory=askdirectory(title = "Select folder")
    root.update()
    root.withdraw()
    print(parent_directory)
    folder=os.listdir(parent_directory)
    for fold in folder:
        os.chdir(parent_directory+"\\"+fold)
        d=os.getcwd()
        i = 0
              
        for filename in os.listdir("."): 
            dst =fold+"_" + str(i) + ".jpg"
            src =d+ "\\" + filename 
            dst =d+ "\\" + dst 
              
            # rename() function will 
            # rename all the files 
            os.rename(src, dst) 
            print(fold,i)
            i += 1