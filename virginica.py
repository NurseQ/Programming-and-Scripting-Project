# James Quintin 20/04/18
# Analysis of the Iris Verginica Flower from Fishers Iris Flower Dataset

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#takes the third 50 of each column which is the iris-Verginica
a = firstcol[100:150]
b = seccol [100:150]
c = thirdcol[100:150]
d = fourthcol[100:150]


#calculate the mean of each of the column
meanDataA = numpy.mean(a)
meanDataB = numpy.mean(b)
meanDataC = numpy.mean(c)
meanDataD = numpy.mean(d)

print("The average petal length of the Iris-Verginica is: ",  meanDataA)
print("The average petal width of the Iris-Verginica is: ",  meanDataB)
print("The average sepal length of the Iris-Verginica is: ",  meanDataC)
print("The average of sepal width of the Iris-Verginica is: ", meanDataD)

# imported library for visualization of data
import matplotlib.pyplot as mp

# command for plotting column a (petal length) into a histogram
# argument can be changed to either column a, b, c or d
mp.hist(a)
# command to print out histogram chart
mp.show()