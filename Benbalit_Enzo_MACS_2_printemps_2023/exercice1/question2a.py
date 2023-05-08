import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr

### QUESTION (a)

def simulerBrownien(T,n):
    h=T/n
    W=np.zeros(n+1)
    for i in range(n):
        W[i+1]=npr.normal(loc=0,scale=np.sqrt(h))+W[i] #W[i+1]=N(0,h)+W[i]
    return W



