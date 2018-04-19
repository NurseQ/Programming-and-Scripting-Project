# James Quintin 
#splitting the arrays
import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# takes the first column of the whole dataset
firstcol = data[:,0]

#takes the first 50 of the first column
x = firstcol[0:50]

#takes the mean of the first column
meanData = numpy.mean(x)

print(meanData)