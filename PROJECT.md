# PROJECT 2018
## PROGRAMMING AND SCRIPTING
The code refers to code written in python
## Background and Summary of Fishers Iris Flower Dataset
The dataset used in this project was introduced by Ronald Fisher in 1936 from his paper "The use of multiple measurements in taxonomic problems". This is considered to be best known database in pattern recognition literature [1]. Fishers Iris flower dataset contains measurements of three classes of Iris flower, the setosa, versicolor and virginica. Measurements from fifty samples are recorded from each of the flowers' petal length, petal width, sepal length and sepal width. Through a statistical method of linear discriminant analysis, Fisher used the measurements "to discriminate the species as distincly as possible[2]." The dataset can be opened or viewed in the repository in a folder named "datum", alternatively, please click here.  
## Investigations regarding the dataset in Python
### Opening csv files
Fishers dataset can be downloaded as a csv file from this site. The code inserted below shows how the csv file was opened using python code. It is then printed out with the main headings added to which the measurements refer. The formatting gives space for each measurement and removes the commas and spaces for a clearer view upon printout. The code can be found by clicking here.

### Counting the dataset
The number of rows within Fishers dataset are counted using the code inserted below. The code takes the first column and uses the range function to count each of the rows. Opening the csv file from the repository will also show the number of rows and columns. 

### Splitting the columns
The code below first splits the dataset into each column then divides each column by fifty. This will assign each group of fifty measurements into each flowers petal length, petal width, sepal length and sepal width. When the measurements are grouped into each flowers appropriate heading, further analysis can be employed. The inserted code under max, min, mean shows code used to calculate the maximum measurements, minimum measurements and the average of each group or heading. 

### Statistical Values

### Histograms
 
## Classification process
The paper by Fisher was found to be mathematically challenging to use as a basis for the conduct of this project. The programming skills of the researcher was also deficient to offer more complex solutions to try and classify the flowers. The paper by Hoey offered a simpler solution and less complicated method to classify the flowers from the dataset. Hoey looked at the dataset and drew patterns to see how each of the class of flowers differed from each other. This project attempts to use Hoey's method to produce a distinction between each of the flowers. The conclusions drawn from this project are generalizations and would require more advanced statistical analysis including standard deviation and variance to offer more accurate distinctions. The use of other python data analytics libraries might also be needed to output more intuitive graphical representation or graphs for a more detailed analysis of the dataset. Figures 1 and 2 show more overlap in the measurements in the dataset which is reflected with narrower distances between the statistical values. Figures 3 and 4 show more distinct separation and is also reflected in the measurements of statistical values.  

**Figure 1** - This scatter plot compares the petal length with the classification of flower. Conclusions drawn from figure 1 are listed below and the maximum, minimum and mean support the listed conclusions. 
1. The Iris Setosa has the shortest petal with a some overlap with the second shortest, the Iris Versicolor. There is also a few overlap with Virginica.
2. The Iris Versicolor has a medium petal in relation to the other flowers but with more overlap with Virginica.
3. The Iris Virginica has the longest petals with much overlap with Versicolor.

![Scatter plot of petal length](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20petal%20length.png)


**Figure 2** - This scatter plot compares the petal width with the classification of flower. There appears to be more overlap in this figure but conclusions can still be drawn from the figure. This is also reflected in the values from the maximum, minimum and mean where the values are numerically closer to each other.  
1. The Iris Setosa has the widest petal but show much overlap with Virginica and some overlap with Versicolor.
2. The Iris Virginica has a medium petal in relation to the other flowers, measurements overlap with both other flowers.
3. The Iris Versicolor has the narrowest petals but has a close overlap with Virginica and some overlap with Setosa.

![Scatter plot petal width](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20petal%20width.png)

**Figure 3** - This scatter plot compares the sepal length with the classification of flower. Conclusions drawn from figure 3 are listed below and the maximum, minimum and mean support the listed conclusions. 
1. The Iris Setosa has the shortest sepal length with no overlap from the other flowers.
2. The Iris Versicolor has a medium sepal length in relation to the other flowers.
3. The Iris Virginica has the longest sepal length with little overlap with the Iris Versicolor.

![Scatter plot sepal length](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20sepal%20length.png)

**Figure 4** - This scatter plot compares the sepal width with the classification of flower. Conclusions drawn from figure 3 are listed below and the maximum, minimum and mean support the listed conclusions. 
1. The Iris Setosa has the narrowest petal with clear distinction from the other flowers.
2. The Iris Versicolor has a medium sepal width in relation to the other flowers.
3. The Iris Virginica has the widest sepals with very little overlap with the Iris Versicolor.

![Scatter plot sepal width](https://github.com/NurseQ/Project-Iris-Flower-Dataset/blob/master/Images/Scatter%20sepal%20width.png)




  
## Suppporting tables and graphs
## References

