# James Quintin 

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

firstcol = data[:,4]

print(firstcol)