# IRIS FLOWER DATA SET PROJECT

This project contains analysis of Fisher's Iris flower dataset. It includes research of the dataset, analysis, documentation and code written in the Python programming language. This is a project for the course Programming and Scripting, in partial fulfillment of the requirements for Higher Diploma in Data Analytics.

## 1. Summary of Fishers Iris Flower Dataset

The dataset used in this project was introduced by Ronald Fisher in 1936 from his paper "The use of multiple measurements in taxonomic problems." This is considered to be best known database in pattern recognition literature [1]. Fishers Iris flower dataset contains measurements of three classes of Iris flower, the setosa, versicolor and virginica. Measurements from fifty samples are recorded from each of the flowers' petal length, petal width, sepal length and sepal width. Through a statistical method of linear discriminant analysis, Fisher used the measurements "to discriminate the species as distincly as possible[2]." The dataset can be opened or viewed in the repository in a folder named [datum](https://github.com/NurseQ/Project-Iris-Flower-Dataset/tree/master/datum). 

## 2. Investigations regarding the dataset in Python
This section presents the steps taken to analyse the data set. A brief narrative to explain the procedure and extracts of code are inserted to present how the data set is manipulated. A link to the whole code is provided for each section.  

### 2a. Opening csv files
Fisher's dataset can be downloaded as a csv file from [UCI machine learning repository](http://archive.ics.uci.edu/ml/machine-learning-databases/iris/). The code inserted below shows how the csv file is opened using python code within this project. There are many ways to open or read csv files, please see [exercise5.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/exercise5.py) in the repository for a different way of reading the same csv file and formatting the output for better readability. 

```python
import numpy
# read the file 
data = numpy.genfromtxt("datum/iris.csv", delimiter=",")
print(data)
```
### 2b. Counting the dataset
The number of rows within Fishers dataset are counted using the code inserted below. The code takes the first column and uses the range function to count each of the rows. Opening the csv file from the repository will also show the number of rows and columns. The code in the repository is [count.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/count.py).  

```python
import numpy

# read the file 
data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first column of the entire dataset
firstcol = data[:,0]

i = 0

# loop to count the length of the first column
while i < len(firstcol):
    # print i and whatever i is in the list
    print(i, firstcol[i]) 
    i = i + 1
```
### 2c. Splitting the columns
The inserted code below first splits the dataset into each column then divides each column by fifty. This will assign each group of fifty measurements into each flowers petal length, petal width, sepal length and sepal width. When the measurements are grouped into each flowers appropriate heading, further analysis can be employed. See this code in the repository [scatpetlength.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/scatpetlength.py).   

```python
import numpy

data = numpy.genfromtxt("datum/iris.csv", delimiter=",")

# splits the array and takes the first 4 columns of the entire dataset
firstcol = data[:,0]
seccol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

#The first column is the petal length and split into each flower
setosaPlength = firstcol[0:50]
versicolorPlength = firstcol [50:100]
virginicaPlength = firstcol[100:150]


```

### 2d. Python libraries
As seen from the sample snippets of code above, the numpy python library is imported. For additional functionality and graphical visualization, matplolib.pyplot is imported and used in the code. Please see two examples inserted below. Code 1 shows use of a plot placing flower measurements in the y axis and the sample number on the x axis. Code 2 shows the petal length of the Iris setosa on the x axis and the petal width on the y axis. See code 1 in the repository [scatpetlength.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/scatpetlength.py), code 2 [setosa.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/setosa.py). 

**Code 1**
```python
# imported library for visualization of data
import matplotlib.pyplot as mp

# provides the x axis with a range up to 50
x = range(0,50)

# command for plotting petal length into a histogram
# argument can be changed to either flower
mp.hist(setosaPlength)
# command to print out histogram chart
mp.show()

# plots each data point to visualize general petal length of flower, adds color to each data point
se = mp.scatter(x,setosaPlength,c="b")
ve = mp.scatter(x,versicolorPlength,c="r")
vi = mp.scatter(x, virginicaPlength, c="g")

# creates a label along the y axis
mp.ylabel("Petal length in cm")

# creates a legend in the graph with appropriate colors 
mp.legend((se,ve,vi),("Setosa", "Versicolor", "Virginica"))
mp.show()
```

**Code 2**

```python

# plots petal length on x axis and petal width on y axis
# arguments can be changed to sepal length and width 
mp.scatter(a,b,c="r")


mp.xlabel("petal length in cm")
mp.ylabel("petal width in cm ")
mp.show()
```

### 2e. Statistical Values
The inserted sample code shows code used to calculate the maximum measurements, minimum measurements and the average of each group or heading. See this code in the repository [scatpetlength.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/scatpetlength.py).   
```python
#calculate the mean, max, min of petal length of each flower
meanDataA = numpy.mean(setosaPlength)
meanDataB = numpy.mean(versicolorPlength)
meanDataC = numpy.mean(virginicaPlength)

minset = numpy.min(setosaPlength)
minver = numpy.min(versicolorPlength)
minvirg = numpy.min(virginicaPlength)

maxset = numpy.max(setosaPlength)
maxver = numpy.max(versicolorPlength)
maxvirg = numpy.max(virginicaPlength)

```

## 3. Observations and Analysis
The paper by Fisher was found to be mathematically challenging to use as a basis for the conduct of this project. The programming skills of the researcher was also deficient to offer more complex solutions to try and classify the flowers. The paper by Hoey [3] offered a simpler solution and less complicated method to classify the flowers from the dataset. Hoey looked at the dataset and drew patterns to see how each of the class of flowers differed from each other. This project attempts to use Hoey's method to produce a distinction between each of the flowers. The conclusions drawn from this project are generalizations and would require more advanced statistical analysis including standard deviation and variance to offer more accurate distinctions. The use of other python data analytics libraries might also be needed to output more intuitive graphical representation or graphs for a more detailed analysis of the dataset.

Figures 1 and 2 show more overlap in the measurements in the dataset which is reflected with narrower distances between the statistical values. Figures 3 and 4 show more distinct separation and is also reflected in the measurements of statistical values.  

**Figure 1** - This scatter plot compares the petal length with the classification of flower. Observations drawn from figure 1 are listed below and the maximum, minimum and mean support the listed conclusions. See the code [scatpetlength.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/scatpetlength.py).
1. The Iris Setosa has the shortest petal with a some overlap with the second shortest, the Iris Versicolor. There is also a few overlap with Virginica.
2. The Iris Versicolor has a medium petal in relation to the other flowers but with more overlap with Virginica.
3. The Iris Virginica has the longest petals with much overlap with Versicolor.

**Statistical values**

The average petal length of the Iris-Setosa is:  5.006\
The average petal length of the Iris-Versicolor is:  5.936\
The average petal length of the Iris-Virginica is:  6.588\
The minimum petal length of the Iris-Setosa is:  4.3\
The minimum petal length of the Iris-Versicolor is:  4.9\
The minimum petal length of the Iris-Virginica is:  4.9\
The maximum petal length of the Iris-Setosa is:  5.8\
The maximum petal length of the Iris-Versicolor is:  7.0\
The maximum petal length of the Iris-Virginica is:  7.9

![Scatter plot of petal length](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20petal%20length.png)


**Figure 2** - This scatter plot compares the petal width with the classification of flower. There appears to be more overlap in this figure but conclusions can still be drawn from the figure. This is also reflected in the values from the maximum, minimum and mean where the values are numerically closer to each other. See the code [scatpetwidth.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/scatpetwidth.py).
1. The Iris Setosa has the widest petal but show much overlap with Virginica and some overlap with Versicolor.
2. The Iris Virginica has a medium petal in relation to the other flowers, measurements overlap with both other flowers.
3. The Iris Versicolor has the narrowest petals but has a close overlap with Virginica and some overlap with Setosa.

**Statistical values**

The average petal width of the Iris-Setosa is:  3.418\
The average petal width of the Iris-Versicolor is:  2.77\
The average petal width of the Iris-Virginica is:  2.974\
The minimum petal width of the Iris-Setosa is:  2.3\
The minimum petal width of the Iris-Versicolor is:  2.0\
The minimum petal width of the Iris-Virginica is:  2.2\
The maximum petal width of the Iris-Setosa is:  4.4\
The maximum petal width of the Iris-Versicolor is:  3.4\
The maximum petal width of the Iris-Virginica is:  3.8
![Scatter plot petal width](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20petal%20width.png)

**Figure 3** - This scatter plot compares the sepal length with the classification of flower. Observations drawn from figure 3 are listed below and the maximum, minimum and mean support the listed conclusions. See the code [scatsepallen.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/scatsepallen.py).
1. The Iris Setosa has the shortest sepal length with no overlap from the other flowers.
2. The Iris Versicolor has a medium sepal length in relation to the other flowers.
3. The Iris Virginica has the longest sepal length with little overlap with the Iris Versicolor.

**Statistical values**

The average sepal length of the Iris-Setosa is:  1.464\
The average sepal length of the Iris-Versicolor is:  4.26\
The average sepal length of the Iris-Virginica is:  5.552\
The minimum sepal length of the Iris-Setosa is:  1.0\
The minimum sepal length of the Iris-Versicolor is:  3.0\
The minimum sepal length of the Iris-Virginica is:  4.5\
The maximum sepal length of the Iris-Setosa is:  1.9\
The maximum sepal length of the Iris-Versicolor is:  5.1\
The maximum sepal length of the Iris-Virginica is:  6.9

![Scatter plot sepal length](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20sepal%20length.png)

**Figure 4** - This scatter plot compares the sepal width with the classification of flower. Observations drawn from figure 3 are listed below and the maximum, minimum and mean support the listed conclusions. See the code [scatsepalwid.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/scatsepalwid.py)
1. The Iris Setosa has the narrowest petal with clear distinction from the other flowers.
2. The Iris Versicolor has a medium sepal width in relation to the other flowers.
3. The Iris Virginica has the widest sepals with very little overlap with the Iris Versicolor.

**Statistical values**

The average sepal width of the Iris-Setosa is:  0.244\
The average sepal width of the Iris-Versicolor is:  1.326\
The average sepal width of the Iris-Virginica is:  2.026\
The minimum sepal width of the Iris-Setosa is:  0.1\
The minimum sepal width of the Iris-Versicolor is:  1.0\
The minimum sepal width of the Iris-Virginica is:  1.4\
The maximum sepal width of the Iris-Setosa is:  0.6\
The maximum sepal width of the Iris-Versicolor is:  1.8\
The maximum sepal width of the Iris-Virginica is:  2.5

![Scatter plot sepal width](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20sepal%20width.png)

**Figure 5** - Scatter plot of the Iris Setosa, plotting petal length on the x axis and petal width on the y axis . It is expected that further anlysis will use similar plots and placing the flower species in the same graph. The code is in [setosa.py](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/setosa.py).

![petal length vs width](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20plot%20petal%20length%20vs%20width.png)

  
### 3a. Histograms
Other supporting graphs used in the project are histograms, which also show the underlying frequency distribution of the dataset. Histograms allow visualization of the shape of continous data including skewness and outliers within the dataset. 

**Setosa petal length histogram** 

![Setosa petal length histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/setA.png)

**Setosa petal width histogram**

![Setosa petal width histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/setB.png)

**Setosa sepal length histogram**

![Setosa sepal length histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/setC.png)

**Setosa sepal width histogram**

![Setosa sepal width histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/setD.png)

**Versicolor petal length histogram** 

![Versicolor petal length histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/versA.png)

**Versicolor petal width histogram** 

![Versicolor petal width histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/versB.png)

**Versicolor sepal length histogram** 

![Versicolor sepal length histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/versC.png)

**Versicolor sepal width histogram** 

![Versicolor sepal width histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/versD.png)

**Virginica petal length histogram** 

![Virginica petal length histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/virA.png)

**Virginica petal width histogram** 

![Virginica petal width histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/virB.png)

**Virginica sepal length histogram** 

![Virginica sepal length histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/virC.png)

**Virginica sepal width histogram** 

![Virginica sepal width histogram](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/virD.png)


## References
[1] UCI Machine Learning Repository, "Iris Data Set," [Online]. Available: https://archive.ics.uci.edu/ml/datasets/iris. [Accessed: April 11,2018].

[2] R. A. Fisher, "The use of multiple measurements in taxonomic problems," *The Annals of Human Genetics, 1936,* [Online] Available: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x. [Accessed: April 11, 2018].

[3] P. S. Hoey, "Statistical analysis of the Iris Flower Dataset", University of Massachusetts, [Online]. Available: http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf. [Accessed: April 11,2018].

