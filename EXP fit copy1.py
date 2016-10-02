# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:00:00 2016

@author: SRINIVAS
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.optimize


def main():
    # Actual parameters
    
    # Generate some data based on these

    y = np.array(list(map(int,['1', '2', '8', '32', '162', '976', '6832', '54663', '491971', '4919711', '54116823', '649401885', '8442224517', '118191143240', '1772867148604', '28365874377664', '482219864420304', '8679957559565488', '164919193631744286', '3298383872634885721'])))
 
    A0, K0, C0 = 2.5, -4.0, y[0]

    t=range(len(y))

    # Add noise
    noisy_y = y

    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)

    # Non-linear Fit

    A, K, C = fit_exp_nonlinear(t, noisy_y)
    fit_y = model_func(t, A, K, C)
    plot(ax1, t, y, noisy_y, fit_y, (A0, K0, C0), (A, K, C0))
    ax1.set_title('Non-linear Fit')

    # Linear Fit (Note that we have to provide the y-offset ("C") value!!

    plt.show()

def model_func(t, A, K, C):
    return A * np.exp(K * t) + C



def fit_exp_nonlinear(t, y):
    opt_parms, parm_cov = sp.optimize.curve_fit(model_func, t, y, maxfev=1000)
    A, K, C = opt_parms
    return A, K, C

def plot(ax, t, y, noisy_y, fit_y, orig_parms, fit_parms):
    A0, K0, C0 = orig_parms
    A, K, C = fit_parms

    ax.plot(t, y, 'k--')
    ax.plot(t, fit_y, 'b-')

    

if __name__ == '__main__':
    main()