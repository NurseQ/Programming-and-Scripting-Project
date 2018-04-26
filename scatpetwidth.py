import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#The second column is the petal width and split into each flower
setosaPwidth = seccol[0:50]
versicolorPwidth = seccol [50:100]
virginicaPwidth = seccol[100:150]



#calculate the mean, max, min of petal width of each flower
meanDataA = numpy.mean(setosaPwidth)
meanDataB = numpy.mean(versicolorPwidth)
meanDataC = numpy.mean(virginicaPwidth)

minset = numpy.min(setosaPwidth)
minver = numpy.min(versicolorPwidth)
minvirg = numpy.min(virginicaPwidth)

maxset = numpy.max(setosaPwidth)
maxver = numpy.max(versicolorPwidth)
maxvirg = numpy.max(virginicaPwidth)


print("The average petal width of the Iris-Setosa is: ",  meanDataA)
print("The average petal width of the Iris-Versicolor is: ",  meanDataB)
print("The average petal width of the Iris-Virginica is: ",  meanDataC)

print("The minimum petal width of the Iris-Setosa is: ",  minset)
print("The minimum petal width of the Iris-Versicolor is: ",  minver)
print("The minimum petal width of the Iris-Virginica is: ",  minvirg)

print("The maximum petal width of the Iris-Setosa is: ",  maxset)
print("The maximum petal width of the Iris-Versicolor is: ",  maxver)
print("The maximum petal width of the Iris-Virginica is: ",  maxvirg)

# imported library for visualization of data
import matplotlib.pyplot as mp
x = range(0,50)

# command to plot each of the flowers petal width into a histogram
# argument can be changed to either flower
mp.hist(setosaPwidth)
# command to print out histogram chart
mp.show()

# plots each data point to visualize general petal width of flower
se = mp.scatter(x,setosaPwidth,c="b")
ve = mp.scatter(x,versicolorPwidth,c="r")
vi = mp.scatter(x, virginicaPwidth, c="g")
mp.ylabel("Petal width in cm")
mp.legend((se,ve,vi),("Setosa", "Versicolor", "Virginica"))
mp.show()