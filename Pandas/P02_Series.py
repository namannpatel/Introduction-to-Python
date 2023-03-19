# Author: NAMAN PATEL

#A Series is a one-dimensional array containing a sequence of values of any data type (int, float, list, string, etc)

#to import pandas library:
import pandas as pd

#1. Creation of Series

#(A) Creation of Series from Scalar Values:
series1 = pd.Series([10,20,30])
print(series1)

#0    10
#1    20
#2    30

#(B) Creation of Series from NumPy Arrays
#We can create a series from a one-dimensional (1D) NumPy array
import numpy as np      # import NumPy with alias np
array1 = np.array([1,2,3,4])
series3 = pd.Series(array1)
print(series3)

#0     1 
#1     2 
#2     3 
#3     4 
#dtype: int32

#we can use letters or strings as indices
series4 = pd.Series(array1, index = ["Jan", "Feb", "Mar", "Apr"])
print(series4)

#Jan    1
#Feb    2
#Mar    3
#Apr    4
#dtype: int32

#(C) Creation of Series from Dictionary
dict1 = {'India': 'NewDelhi', 'UK': 'London', 'Japan': 'Tokyo'}
print(dict1)      #Display the dictionary
#{'India': 'NewDelhi', 'UK': 'London', 'Japan': 'Tokyo'}
series8 = pd.Series(dict1)
print(series8)    #Display the series

#India    NewDelhi
#UK         London
#Japan       Tokyo
#dtype: object

#2.Accessing Elements of a Series

#(A) Indexing
#usage of positional index for accessing a value
seriesNum = pd.Series([10,20,30])
seriesNum[2]

#30
