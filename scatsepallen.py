# James Quintin 16/04/18
# Analysis of the Iris Setosa Flower from Fishers Iris Flower Dataset

import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#The first column is the sepal length and split into each flower
setosaSlength = thirdcol[0:50]
versicolorSlength = thirdcol [50:100]
virginicaSlength = thirdcol[100:150]



#calculate the mean, max, min of sepal length of each flower
meanDataA = numpy.mean(setosaSlength)
meanDataB = numpy.mean(versicolorSlength)
meanDataC = numpy.mean(virginicaSlength)

minset = numpy.min(setosaSlength)
minver = numpy.min(versicolorSlength)
minvirg = numpy.min(virginicaSlength)

maxset = numpy.max(setosaSlength)
maxver = numpy.max(versicolorSlength)
maxvirg = numpy.max(virginicaSlength)


print("The average sepal length of the Iris-Setosa is: ",  meanDataA)
print("The average sepal length of the Iris-Versicolor is: ",  meanDataB)
print("The average sepal length of the Iris-Virginica is: ",  meanDataC)

print("The minimum sepal length of the Iris-Setosa is: ",  minset)
print("The minimum sepal length of the Iris-Versicolor is: ",  minver)
print("The minimum sepal length of the Iris-Virginica is: ",  minvirg)

print("The maximum sepal length of the Iris-Setosa is: ",  maxset)
print("The maximum sepal length of the Iris-Versicolor is: ",  maxver)
print("The maximum sepal length of the Iris-Virginica is: ",  maxvirg)

# imported library for visualization of data
import matplotlib.pyplot as mp
x = range(0,50)

# command for plotting sepal length into a histogram
# argument can be changed to either flower
mp.hist(setosaSlength)
# command to print out histogram chart
mp.show()

# plots each data point to visualize general sepal length of flower
se = mp.scatter(x,setosaSlength,c="b")
ve = mp.scatter(x,versicolorSlength,c="r")
vi = mp.scatter(x, virginicaSlength, c="g")
mp.ylabel("Sepal length in cm")
mp.legend((se,ve,vi),("Setosa", "Versicolor", "Virginica"))
mp.show()