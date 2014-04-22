# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:35:39 2014

@author: swalters
"""

import numpy
import random

def makeTransition():
    LA = [[0.18, 0.5, 0.15], [0.6, 0.5, 0.75], [0.22, 0, 0.1]]
    LD = [[0, 0.25, 0.9], [0, 0, 0.1], [1, 0.75, 0]]
    LG = [[0.4, 0.5, 1], [0.4, 0.25, 0], [0.2, 0.25, 0]]

    return [numpy.matrix(LA), numpy.matrix(LD), numpy.matrix(LG)]
    
# memoize?
# sampling wheel
def predict(k, currentState, prevState):
    [a, d, g] = makeTransition()
    
    p = numpy.matrix(prevState)
    c = numpy.matrix(currentState)
    
    L = None
    for i in range(k):
        # choose transition matrix
        if p[0,0] == 1: L = a
        elif p[1,0] == 1: L = d
        else: L = g
        
        # compute next
        p = samplingWheel(c)
        c = samplingWheel(L*c)
    print c

def samplingWheel(a):
    r = random.random()
    if 0 < r < a[0,0]:
        return numpy.matrix([[1],[0],[0]])
    elif a[0,0] < r < a[1,0]+a[0,0]:
        return numpy.matrix([[0],[1],[0]])
    else:
        return numpy.matrix([[0],[0],[1]])

import numpy as np
from scipy.io.wavfile import write

data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
print data
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
print scaled
write('test.wav', 44100, scaled)