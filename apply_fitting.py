'''
    Apply moving average algorithm
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, csv, datetime, time, subprocess

from numpy import sqrt, pi, exp, linspace, loadtxt
from lmfit import Model
from scipy.optimize import curve_fit
from convert_to_r import ConvertToR

class FittingRegression:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        x_append = x
        y_append = y
        size_array = len(x)
        
        for i in range(0, 2):
            x_append = np.append(x_append, x[i])
            y_append = np.append(y_append, y[i])
        self.apply_mavg(size_array, x_append, y_append)
    
    def apply_mavg(self, size, x_value, y_value):
        
        x_train = []
        y_train = []
        
        result_path = "./fitting_result/mavg_result/fitting_result_"+str(int(round(time.time()*1000)))
        csv_file ="csv_result.csv"
        mse_file ="mse_rate.csv"
        csv_path = result_path+"/csv_result/"
        
        figure = plt.figure()
        figure_path = result_path+"/fitting_graph/"

        array_mse = []
        
        for j in range(0, size):
            x_train.append((x_value[j+2]+x_value[j+1]+x_value[j])/3)
            y_train.append((y_value[j+2]+y_value[j+1]+y_value[j])/3)

        # Write result into csv file
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
            with open(os.path.join(csv_path, csv_file), 'wb') as csv_file:
                file_writer = csv.writer(csv_file)
                print "\n Loading result into csv... \n \n "
                for j in range(0, len(x_train)):
                    file_writer.writerow([x_train[j], y_train[j]])
                    array_mse.append(((y_train[j] - y_value[j])**2))
        print "----- csv result is saved! ------ \n \n "

        # write mse result into csv file
        with open(os.path.join(csv_path, mse_file), 'wb') as csv_mse:
            file_mse = csv.writer(csv_mse)
            mse_value = sum(array_mse)/size
            print "mse_value: ", mse_value
            print "Loading MSE result into csv... \n \n "
            file_mse.writerow([mse_value])

        # save fiting result
        if not os.path.exists(figure_path):
            os.makedirs(figure_path)
            plt.plot(x_value, y_value, 'b-');
            plt.grid(True)
            plt.plot(x_train, y_train, 'r-')
            figure.savefig(figure_path+"fitting_graph.png")

        print "----- Fitting result with moving average is saved! \n \n \n ------"
        ConvertToR(str(x_train), str(y_train))


