import modelproject
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import sympy as sm


def simulate_basic(k,alpha,delta,s,n,g,K,T,D):
    """
    Args:
    k      (int)  : initial value for physical capital per worker
    alpha  (float): return on physical capital
    delta  (float): depreciation rate on capital
    s      (float): savings/investments
    n      (float): increase in labour
    g             : growth
    K      (int)  : totalfactorproductivity
    T      (int)  : periods to simulate through
    D             : climate change
    
    Returns:
    A plot showing how capital per worker accumulates over time"""
    
    #First we make a list for our future values to be in
    k_path = [k]
    
    #Then we make which will contain the values for the 45-degree-line
    Degreeline = [0]
    
    #We generate the 45-degree-line for the basic Solow model
    for t in range(1,T):
        line = (n+g+delta)*t
        Degreeline.append(line)
        
    #We generate the Solow movement
    for t in range(1,T):
        k_plus = s*(1-D)*K*t**alpha
        k_path.append(k_plus)
    
    #Plotting the stuff
    plt.figure(figsize=(7,7))
    plt.plot(k_path[:T], label='$s(1-D)k_t^{\u03B1}$', color = 'red')
    plt.plot(Degreeline[:T], label = '$k_t(n+\delta+g)$', color = 'blue')
    plt.xlim(0,T)
    plt.ylim(0,Degreeline[-1])
    plt.xlabel('$k_t$')
    plt.grid(True)
    plt.legend()
    
    return plt.show()


#Simulation:

def solow_equation(k,alpha,delta,s,n,g, D):
    """ calculate capital in the next-period
        
    Args:
    
        k (float): capital in this period
        alpha (float): cobb-douglas parameter
        delta (float): depreciation rate
        s (float): saving rate
        n : population growth
        g : technology growth
    
    Returns:
    
        k_plus (float): capital in next period
        
    """
    
    saving = s*k**alpha
    depreciation = delta*k
    k_plus = (k + saving*(1-D) - depreciation)/((1+n)*(1+g))    
    
    return k_plus


def simulate_solow_model(k0,alpha,delta,s,n,g,T,D):
    """ simulate the solow model
        
    Args:
    
        k0 (float): initial level of kapital
        alpha (float): cobb-douglas parameter
        delta (float): depreciation rate
        s (float): saving rate
        T (int): number of periods to simulate
    
    Returns:
    
        k_path (list): capital path (length T)
        
    """
    
    # a. initialize
    k_path = [k0]  
    
    # b. simulate forward
    for t in range(1,T):
        
        # i. apply solow equation
        k_plus = solow_equation(k_path[t-1],alpha,delta,s,n,g,D)    
        
        # ii. save result
        k_path.append(k_plus)
        
    return k_path


def find_ssk_k(delta,g,n,alpha,s,D):
    return ((delta+g*n+g+n)/(s*(1-D)))**(1/(alpha-1))

def ss(n)
    return n