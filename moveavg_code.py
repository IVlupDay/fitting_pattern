#code to implement python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, csv, datetime, time, subprocess

from numpy import sqrt, pi, exp, linspace, loadtxt
from lmfit import Model
from scipy.optimize import curve_fit

data = pd.read_csv("csv_data.csv", sep=';', names=['x', 'y'])
print "%%%%---------------- SUCEESS LOAD ----------------%%%%"
print "Result...\n \n \n "

figure = plt.figure()

csv_file ="csv_result.csv"
mse_file ="mse_rate.csv"
result_path = "./fitting_result_"+str(int(round(time.time()*1000)))
csv_path = result_path+"/csv_result/"
figure_path = result_path+"/fitting_graph/"

x = data.values[:, 0]
y = data.values[:, 1]
size = len(data.values[:, 0])

for i in range(0, 2):
    x = np.append(x, data.values[i,0])
    y = np.append(y, data.values[i,1])

peak_x = []
peak_y = []
array_mse = []

for j in range(0, size):
    peak_x.append((x[j+2]+x[j+1]+x[j])/3)
    peak_y.append((y[j+2]+y[j+1]+y[j])/3)

# Write result into csv file
if not os.path.exists(csv_path):
    os.makedirs(csv_path)
    with open(os.path.join(csv_path, csv_file), 'wb') as csv_file:
        file_writer = csv.writer(csv_file)
        print "\n Loading result into csv... \n \n "
        for j in range(0, len(peak_y)):
            file_writer.writerow([peak_x[j], peak_y[j]])
            array_mse.append(((peak_y[j] - data.values[j, 1])**2))
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
    plt.plot(x, y, 'b-');
    plt.grid(True)
    plt.plot(peak_x, peak_y, 'r-')
    figure.savefig(figure_path+"fitting_graph.png")
print "----- Figure result is saved! ------"

print "Result...\n \n \n "
print "%%%%-------------- SUCEESS FITTING --------------%%%%"





