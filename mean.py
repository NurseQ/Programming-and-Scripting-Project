# James Quintin, 18/04/18
#Analysis of iris csv

#calculate mean

import numpy

# Read data file into array
data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

#takes data from first number of each array
firstcol = data[:,0]

#takes the average/mean of the first numbers of the array
meanData = numpy.mean(firstcol)

print(meanData)


