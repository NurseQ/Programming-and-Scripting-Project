# James Quintin 21/04/18
# Analysis of the petal length of the 3 Iris' from Fishers Iris Flower Dataset

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array generates the first column of the dataset
firstcol = data[:,0]


# splits the first column into the petal length of setosa, versicolor, virginica
a = firstcol[0:50]
b = firstcol [50:100]
c = firstcol[100:150]



#calculate the mean of the petal lengths
meanDataA = numpy.mean(a)
meanDataB = numpy.mean(b)
meanDataC = numpy.mean(c)


print("The average petal length of the Iris-Setosa is: ",  meanDataA)
print("The average petal length of the Iris-Versicolor is: ",  meanDataB)
print("The average sepal length of the Iris-Verginica is: ",  meanDataC)


# imported library for visualization of data
import matplotlib.pyplot as mp

# command for plotting column (petal length) into a histogram
# argument can be changed to either a, b, c petal lengths
mp.hist(a)
# command to print out histogram chart
mp.show()