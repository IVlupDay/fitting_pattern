#code to implement python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, csv, datetime, time, subprocess

from numpy import sqrt, pi, exp, linspace, loadtxt
from lmfit import Model
from scipy.optimize import curve_fit
from apply_fitting import FittingRegression

print "\n%%%%---------------- SUCEESS LOAD ----------------%%%%\n"

'''
name = raw_input("What name?")
users[name] = User(name)
'''

data = pd.read_csv("./input_data/csv_data.csv", sep=';', names=['x', 'y'])

x = data.values[:, 0]
y = data.values[:, 1]
size = len(data.values[:, 0])

print "----- Apply moving average on data ------\n \n \n"
#MovingAverage.execute_mavg(x, y)
FittingRegression(x,y)
