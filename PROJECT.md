# PROJECT 2018
## PROGRAMMING AND SCRIPTING
```python
# James Quintin 20/04/18
# Analysis of the Fishers Iris Flower Dataset

# Count the number of rows, counting the first column

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
 

