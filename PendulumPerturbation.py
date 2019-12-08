# -*- coding: utf-8 -*-
"""
Pendulum_Perturbation.py is a script that does analysis on a double pendulum,
specifically on the divergence in trajectories for double pendulums with similar
but slightly varying initial conditions.

Team Lead: Jorge Ramirez
Engine code: Angel Torres
Analysis: Maia Adams

Supervised by Dan Lathrop as a part of the University of Maryland, College Park
PHYS410: Classical Mechanics

"""

"""
This code is split into three sections.

    [0] simulation settings
        a chunk of code dedicated to simulation settings that are global
        throughout the entire script
        
    [1] numerical computation
        a chunk of code dedicated to the numerical computation of 
        double pendulum trajectories    
    
    [2] analytics
        a chunk of code dedicated to running analytics on the computations,
        e.g. lyapunov exponent, chaos measurements, etc
        
    [3] plotting algorithm
        a chunk of code dedicated to creating visual representations of the
        various double pendulum trajectories in an aesthetically-pleasing
        realtime plot format.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp



'''
===============================================================================
[0] simulation settings
    Inputs -
        user defined constants
        universal constants
    Outputs - 
        global variables to be used in [1] [2] (3)
===============================================================================        
'''

# first declare our simulation variables

m1, m2 = 1, 1  # pendulum mass 1 and mass 2  [kg]
l1, l2 = 1, 1  # pendulum length 1 and length 2 [meters]
g = 9.81  # gravitational acceleration


init_conditions = (g, m1, m2, l1, l2)




'''
===============================================================================
[1] numerical computation (Angel Torres)
    Inputs - 
        time series 
        global settings
        
    Outputs -
        array of computed trajectory from section
===============================================================================     
'''

def double_pen(z, t, glo):
    theta1, T1, theta2, T2 = z
    m1, m2, l1, l2, g = glo
    C = np.cos(theta1 - theta2)
    c2 = np.cos(2*theta1 - 2*theta2)
    S = np.sin(theta1-theta2)
    M = m1+m2
    
#Simplifications for repetition between ODES for theta1doubledot and theta2doubledot 
    f = [T1,T1d = (-g*(2*m1+m2)*np.sin(theta1)-m2*g*S-2*S*m2*((T2**2)*l2+T1**2*l1*C))/(l1*(2*m1+m2-m2*c2)), \
         T2, T2d = (2*S*((T1**2)*l1*M+g*M*np.cos(theta1)+(T2**2)*l2*m2*C))/(l2*(2*m1+m2-m2*c2))]
#Four 1st Order Equations for the Coupled Second Order ODEs
    theta1_dot = T1
    theta2_dot = T2
    theta1_dotdot = (-g*(2*m1+m2)*np.sin(theta1)-m2*g*S-2*S*m2*((T2**2)*l2+T1**2*l1*C))/(l1*(2*m1+m2-m2*c2))
    theta2_dotdot = (2*S*((T1**2)*l1*M+g*M*np.cos(theta1)+(T2**2)*l2*m2*C))/(l2*(2*m1+m2-m2*c2))
    
#T1 is the first derivative of theta1, T2 is the first for theta2
#T1d is the second derivative of theta1, T2d is the second for theta2
    
    return theta1_dot, theta2_dot, theta1_dotdot, theta2_dotdot  


def simulate_pendulum(time_series, init_cond, global_settings):
    """
  
    a method that simulates the trajectory of ONE pendulum for a given
    init cond and time series
        
        Inputs - 
            time_series: 
                [float array] a numpy array containing time steps
                created using numpy.linspace
              
            init_cond: 
                [tuple] a tuple of the form (Є1, Є2) where 
                Є1 is shift in θ1 and Є2 is shift in θ2
                
            global_settings: 
                [tuple] a tuple containing the simulation parameters
                        see section [0] for more info
  
        Outputs -
            sim_trajectory:
                [2xn array] a 2D array where column 1 and 2 contain the final 
                trajectory for θ1 and θ2, where n is the total steps
                
    """
    
        
    sim_trajectory = [0, 1, 2]  # contains computed values for f(θ1) and f(θ2) 
    
    return sim_trajectory
            




'''
===============================================================================
[2] analytics (Maia Adams)
    Inputs -
        time series
        array of computed trajectory from section [1]
        
    Outputs - 
        lyapunov exponent
        evolution of chaos??
        divergence of phase-space curves??
===============================================================================
'''

t = np.linspace(0, 5, 0.1)
traj = []

def lyapunov_exponent():
    
    pass

def lyapunov_exp(sim_trajectory, time):
    
        delta = np.abs(sim_trajectory[1]-sim_trajectory[0]) # takes the difference
                                                        #between trajectories   
                                                        #f(θ1) and f(θ2)
        lyapunov = np.log(delta)/time #lyapunov exponent
   
    return lyanpunov




'''
===============================================================================
(3) plotting algorithms (Jorge Ramirez)
    Inputs - 
        time series
        array of computed trajector from sectino [1]
    
    Outputs -
        nxn plot of realtime pendulums
===============================================================================
'''
