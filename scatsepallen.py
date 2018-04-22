# James Quintin 16/04/18
# Analysis of the Iris Setosa Flower from Fishers Iris Flower Dataset

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#The first column is the petal length and split into each flower
setosaSlength = thirdcol[0:50]
versicolorSlength = thirdcol [50:100]
virginicaSlength = thirdcol[100:150]



#calculate the mean of petal length of each flower
meanDataA = numpy.mean(setosaSlength)
meanDataB = numpy.mean(versicolorSlength)
meanDataC = numpy.mean(virginicaSlength)


print("The average petal length of the Iris-Setosa is: ",  meanDataA)
print("The average petal length of the Iris-Versicolor is: ",  meanDataB)
print("The average petal length of the Iris-Virginica is: ",  meanDataC)

# imported library for visualization of data
import matplotlib.pyplot as mp
x = range(0,50)

# command for plotting sepal length into a histogram
# argument can be changed to either flower
mp.hist(setosaSlength)
# command to print out histogram chart
mp.show()

# plots each data point to visualize general petal length of flower
mp.scatter(x,setosaSlength,c="b")
mp.scatter(x,versicolorSlength,c="r")
mp.scatter(x, virginicaSlength, c="g")
mp.ylabel("Sepal length in cm")

mp.show()