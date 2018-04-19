# James Quintin 03/03/18
# Exercise 5 

# command to open file without need for closing the file
with open("datum/iris.csv") as f:
    # print as a header for the values
    print("petal length " "petal width " "sepal length " "sepal width "" Iris Name")
    
    # reads contents of the file line by line, fixes formatting error, rather than using end command.
    for line in f:
        #removes \n from end of each list
        line = line.strip()
        # splits each line into separate list
        line = line.split(',')
        
        #prints spaces between strings, columns, Trial and error.
        print('{:^12}{:^14}{:^10}{:^15}{:15}'.format(line[0],line[1],line[2],line[3],line[4],))
        
