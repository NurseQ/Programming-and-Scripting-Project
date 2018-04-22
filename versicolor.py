# James Quintin 20/04/18
# Analysis of the Iris Versicolor Flower from Fishers Iris Flower Dataset

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#takes the second 50 of each column which is the iris-Versicolor
a = firstcol[50:100]
b = seccol [50:100]
c = thirdcol[50:100]
d = fourthcol[50:100]


#calculate the mean of each of the column
meanDataA = numpy.mean(a)
meanDataB = numpy.mean(b)
meanDataC = numpy.mean(c)
meanDataD = numpy.mean(d)

print("The average petal length of the Iris-Versicolor is: ",  meanDataA)
print("The average petal width of the Iris-Versicolor is: ",  meanDataB)
print("The average sepal length of the Iris-Versicolor is: ",  meanDataC)
print("The average of sepal width of the Iris-Versicolor is: ", meanDataD)

# imported library for visualization of data
import matplotlib.pyplot as mp

# command for plotting column a (petal length) into a histogram
# argument can be changed to either column a, b, c or d
mp.hist(a)
# command to print out histogram chart
mp.show()

# plots petal length on x axis and petal width on y axis
mp.scatter(a,b)
mp.show()