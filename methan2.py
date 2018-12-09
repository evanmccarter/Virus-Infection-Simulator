#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
np.set_printoptions(suppress=True)

def SIR(n, N, R, p, Y_0):
    # suseptible, infected, recovered population
    t = 0     # count
    y = Y_0   # num infected at beginning

    Y = np.zeros((R,), dtype=int)  # Initialize the array with R ints
    Y[0] = y
   
    X = n - y # num people suseptible (can be infected)
    Z = 0     # num recovered at beginning

    total_sum_run = y

    #print "\nSimulation #\t\tDuration\t\t# Infected\n-------------          ------------            -------------"
    #print t, "\t\t\t", t, "\t\t\t", y

    # loop
    while(np.sum(Y) > 0):
        q = 1 - (1- ((p*y)/(n-1)))**N   # prob one individual become infected
        y_run = np.random.binomial(X, q)    # new num people infected
        
        total_sum_run += y_run  # increment total sum run by num newly infected

        X = X - y_run   # reduce num suseptible by num recently infected
        Z = Z + Y[R - 1] # increase num recovered by last spot of time sick array 
        
        # shift the time sick array (Y) over by onei, put new num infected at beginning
        Y = np.roll(Y, 1)
        Y[0] = y_run

        # update total num infected (y) with array with new infected (y_run)
        y = np.sum(Y)

        t += 1 
        #print t, "\t\t\t", t, "\t\t\t", y, Y

    return t, total_sum_run
    print ""

    #print "n: ", n, "   N: ", N, "   R: ", R, "   p: ", p, "   Y_0: ", Y_0, "   t: ", t, "   y: ", y, "   Y: ", Y, "   X: ", X, "   Z: ", Z


def main():
    num_sims = 20
    
    n = 1000   # population size
    N = 4     # number of population contacts
    R = 3     # recovery period
    p = 0.1   # probalbilty of tranmision of disease
    Y_0 = 2   # num people infected at beginning
   
    sum_duration = 0
    total_infected = 0

    print "\nSimulation #\t\tDuration\t\t# Infected\n-------------          ------------            -------------"
    for i in range(num_sims):
        duration, sum_infected = SIR(n, N, R, p, Y_0)
        sum_duration += duration
        total_infected += sum_infected
        print i+1, "\t\t\t", duration, "\t\t\t", sum_infected

    print "-------------          ------------            -------------"
    print "mean\t\t\t", float(sum_duration)/num_sims, "\t\t\t", float(total_infected)/num_sims, "\n"


if __name__=="__main__":
    main()


