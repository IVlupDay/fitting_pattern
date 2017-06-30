#code to implement python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, csv, datetime, time, subprocess
import rpy2.robjects as robjects

from numpy import sqrt, pi, exp, linspace, loadtxt
from lmfit import Model
from scipy.optimize import curve_fit

class ConvertToR:
    def __init__(self, x_mavg, y_mavg):
        #print "Kernel Regression Reached", x_mavg[0]
        #print "Size", len(x_mavg)
        self.x_mavg = x_mavg
        self.y_mavg = y_mavg
        self.apply_kernel_regression(x_mavg, y_mavg)
    
    def apply_kernel_regression(self, x_mavg, y_mavg):
        print "%%%%---------------- Apply Kernel Regression ----------------%%%%"
        
        '''
        # Define command and arguments
        command = 'Rscript'
        script_path = './r_script/apply_kernel_regression.r'
        
        args = [x_mavg, y_mavg]
        #args = ['11', '3']

        # Build subprocess command
        cmd = [command, script_path] + args
        
        # check_output will run the command and store to result
        #subprocess.check_output(cmd, universal_newlines=True)
        subprocess.Popen(["Rscript", script_path, ]) 
        '''
        apply_kernel_regression = robjects.r(r''',library(graphics)''')










