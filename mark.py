# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:13:17 2014

@author: swalters
"""

import numpy

def makeRegular():
    ''' generates regular transition matrix to represent Mark's clothing choices
        input: none
        output: numpy array
    '''
    r1 = [1/float(5), 2/float(3), 1/float(4)]
    r2 = [1/float(5), 0/float(3), 1/float(4)]
    r3 = [3/float(5), 1/float(3), 2/float(4)]

    arrayL = [r1, r2, r3]
    return numpy.matrix(arrayL)
    
def makeAbsorbing():
    ''' generates absorbing transition matrix to represent Mark's clothing choices
        input: none
        output: numpy array
    '''
    r1 = [1, 2/float(3), 1/float(4)]
    r2 = [0, 0/float(3), 1/float(4)]
    r3 = [0, 1/float(3), 2/float(4)]
    
    arrayL = [r1, r2, r3]
    return numpy.matrix(arrayL)
    
def predict(L, k, currentState): # current state in [[1],[0],[0]] format - column matrix
    ''' predicts probabilities k states from currentState
        input: numpy transition matrix array L, integer k, current state vector
            currentState must be in format [[1],[0],[0]]
        output: numpy array representing probabilites k states from currentState
    '''
    x = numpy.matrix(currentState)
    return L**k*x