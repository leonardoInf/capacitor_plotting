"""
File: plotting.py
Author: https://github.com/leonardoInf
Date: 30.10.2019
=================================
Graphically display a .csv file with measurements of a capacitor
and fit a limited exponential growth curve using linear regression.

Specification the csv file:
=================================
Filename: data.csv (can be changes using function_plotting.py <.csv file>)

First line: Title of the graph
Second line: Label for the x-axis
Third line: Label for the y-axis 
Fourth line: Range tuple (startvalue, endvalue, step)
Fifth line: Ignored line (e.g. dashes or blank line) to seperate the header from the actual data
Following lines: y values (data) - seperated by commata

The file data.csv in the same directory as this script provides an example.

Mathematical description:
=================================
The general exponential equation of a capacitor charging curve is:
f(x) = U_B * (1-exp(-t/tau)), whereas tau = R*C.

We split the equation into two parts:
f(x) = g(x) + h(x)
g(x) = U_B
h(x) = U_B * exp(-t/tau)

We transform function h into a linear equation:
h(x) = U_B * exp(-t/tau)    | ln
ln(h(x)) = -t/tau + ln(U_B) | y:= ln(h(x)), c:= 1/tau, d:= ln(U_B)
-> y = c*t + d

Whereas:
tau = 1/c
U_B = exp(d)

We establish a linear system generated using the input data in the .csv file.
We solve Ax = b according to the least square problem using the numerical library numpy.
Our goal is to optimize the parameters c and d. 
"""

import matplotlib.pyplot as plt     # Function plotting
import numpy as np                  # arrays and matrices, linear systems solver
import os                           # Operating System
import sys                          # System (command line arguments)

data_label = ""                     # label for user data (specified by data.csv)
fitted_label = ""                   # label for the fitted data (specified by data.csv)


def calculate():
    t, data = read_data()             # read user data
    tau, U_B = curve_fitting(t, data) # solve least square problem
    fitted_vals = [U_B * (1-np.exp(-t_i/tau)) for t_i in t]  # calculate for fitted values
    return (t, data, fitted_vals, tau, U_B)

def read_data():
    global data_label, fitted_label
    with open(get_filename(), "r") as fobj:                                 # open csv file
        lines = list(fobj)                                                  # read every line into list
        plt.gcf().canvas.set_window_title(lines[0].split()[:2])             # set window title
        plt.title(lines[0])                                                 # set figure title
        data_label = lines[1]                                               # set data label
        fitted_label = lines[2]                                             # set fitted data label
        plt.xlabel(lines[3])                                                # set t label
        plt.ylabel(lines[4])                                                # set y label
        range_tuple = tuple(eval(lines[5]))                                 # range for x values
        t = np.arange(range_tuple[0], range_tuple[1]+10, range_tuple[2])    # create numpy array for x range
        data = list(map(float, lines[7:]))                                  # convert data to float
        return (t, data)
         
def get_filename():
    try:
        return sys.argv[1]
    except:
        return os.path.join(os.getcwd(),"data.csv")
        
def curve_fitting(t, data):
    A = np.matrix([[val, 1] for val in t])              # define coefficient matrix using list comprehension
    b = np.array([data_point for data_point in data])   # define result vector
    c,d = np.linalg.lstsq(A,b, rcond=None)[0].tolist()  # solve least square problem
    return (1/c,np.exp(d))                              # return transformed parameters
    
        
if __name__ == "__main__":    # if this is the main module...
    t, data, fitted_data, tau, U_B = calculate()  # do computations based on user data
    
    plt.plot(t, data, "ko-", label=data_label)    # Plot user data. Format string: k: black, o: circles, -: solid line
    plt.plot(t, fitted_data, label=fitted_label + " {}*[1-e^(-t/{}))]".format(round(U_B,1), round(tau,0)))  # Plot fitted curve
    plt.legend(loc="bottom right")                # add legend
    plt.show()                                    # display interactive graph