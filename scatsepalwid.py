import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#The first column is the sepal width and split into each flower
setosaSwidth = fourthcol[0:50]
versicolorSwidth = fourthcol [50:100]
virginicaSwidth = fourthcol[100:150]



#calculate the mean,max, min of sepal width of each flower
meanDataA = numpy.mean(setosaSwidth)
meanDataB = numpy.mean(versicolorSwidth)
meanDataC = numpy.mean(virginicaSwidth)

minset = numpy.min(setosaSwidth)
minver = numpy.min(versicolorSwidth)
minvirg = numpy.min(virginicaSwidth)

maxset = numpy.max(setosaSwidth)
maxver = numpy.max(versicolorSwidth)
maxvirg = numpy.max(virginicaSwidth)


print("The average sepal width of the Iris-Setosa is: ",  meanDataA)
print("The average sepal width of the Iris-Versicolor is: ",  meanDataB)
print("The average sepal width of the Iris-Virginica is: ",  meanDataC)

print("The minimum sepal width of the Iris-Setosa is: ",  minset)
print("The minimum sepal width of the Iris-Versicolor is: ",  minver)
print("The minimum sepal width of the Iris-Virginica is: ",  minvirg)

print("The maximum sepal width of the Iris-Setosa is: ",  maxset)
print("The maximum sepal width of the Iris-Versicolor is: ",  maxver)
print("The maximum sepal width of the Iris-Virginica is: ",  maxvirg)

# imported library for visualization of data
import matplotlib.pyplot as mp
x = range(0,50)

# command to plot each of the flowers sepal width into a histogram
# argument can be changed to either flower
mp.hist(setosaSwidth)
# command to print out histogram chart
mp.show()

# plots each data point to visualize general sepal width of flower
se = mp.scatter(x,setosaSwidth,c="b")
ve = mp.scatter(x,versicolorSwidth,c="r")
vi = mp.scatter(x, virginicaSwidth, c="g")
mp.ylabel("Sepal width in cm")
mp.legend((se,ve,vi),("Setosa", "Versicolor", "Virginica"))
mp.show()