# James Quintin 
#splitting the arrays
import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# takes the first column of the whole dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]
#takes the first 50 of the first column
a = firstcol[0:50]
b = seccol [0:50]
c = thirdcol[0:50]
d = fourthcol[0:50]


#takes the mean of the first column
meanDataA = numpy.mean(a)
meanDataB = numpy.mean(b)
meanDataC = numpy.mean(c)
meanDataD = numpy.mean(d)
print(meanDataA, meanDataB, meanDataC, meanDataD)