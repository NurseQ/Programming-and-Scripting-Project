# James Quintin 16/04/18
# Analysis of the Iris Setosa Flower from Fishers Iris Flower Dataset

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#takes the first 50 of each column which is the iris-setosa
a = firstcol[0:50]
b = seccol [0:50]
c = thirdcol[0:50]
d = fourthcol[0:50]


#calculate the mean of each of the column
meanDataA = numpy.mean(a)
meanDataB = numpy.mean(b)
meanDataC = numpy.mean(c)
meanDataD = numpy.mean(d)

print("The average petal length of the Iris-Setosa is: ",  meanDataA)
print("The average petal width of the Iris-Setosa is: ",  meanDataB)
print("The average sepal length of the Iris-Setosa is: ",  meanDataC)
print("The average of sepal width of the Iris-Setosa is: ", meanDataD)

# imported library for visualization of data
import matplotlib.pyplot as mp

# command for plotting column a (petal length) into a histogram
# argument can be changed to either column a, b, c or d
mp.hist(a)
# command to print out histogram chart
mp.show()

# plots petal length on x axis and petal width on y axis
# arguments can be changed to sepal length and width 
mp.scatter(a,b,c="r")


mp.xlabel("petal length in cm")
mp.ylabel("petal width in cm ")
mp.show()