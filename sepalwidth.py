# James Quintin 22/04/18
# Analysis of the sepal width of the 3 Iris' from Fishers Iris Flower Dataset

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array generates the first column of the dataset
col = data[:,3]


# splits the first column into the sepal width of setosa, versicolor, virginica
a = col[0:50]
b = col [50:100]
c = col[100:150]



#calculate the mean of the sepal widths
meanDataA = numpy.mean(a)
meanDataB = numpy.mean(b)
meanDataC = numpy.mean(c)


print("The average sepal width of the Iris-Setosa is: ",  meanDataA)
print("The average sepal width of the Iris-Versicolor is: ",  meanDataB)
print("The average sepal width of the Iris-Verginica is: ",  meanDataC)


# imported library for visualization of data
import matplotlib.pyplot as mp

# command for plotting column (sepal width) into a histogram
# argument can be changed to either a, b, c sepal widths
mp.hist(a)
# command to print out histogram chart
mp.show()