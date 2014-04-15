# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:13:17 2014

@author: swalters
"""

import numpy

r1 = [1/float(5), 2/float(3), 1/float(4)]
r2 = [1/float(5), 0/float(3), 1/float(4)]
r3 = [3/float(5), 1/float(3), 2/float(4)]

arrayL = [r1, r2, r3]
L = numpy.matrix(arrayL)
print L**100