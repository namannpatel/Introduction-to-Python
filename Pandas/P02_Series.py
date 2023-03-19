# Author: NAMAN PATEL

#A Series is a one-dimensional array containing a sequence of values of any data type (int, float, list, string, etc)

#to import pandas library:
import pandas as pd

#1. Creation of Series

#syntax: <Series Object> = pandas.Series(data, index=idx)
#where idx is a valid numpy datatype
#and data can be created using
#A Python Sequence
#An ndarray
#A Python Dictionary
#A scalar value

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
#syntax: <Series Object name>[<valid indexes>]
seriesNum = pd.Series([10,20,30])
seriesNum[2]                         #30
seriesCapCntry = pd.Series(['NewDelhi', 'WashingtonDC', 'London', 'Paris'],
index=['India', 'USA', 'UK', 'France'])
seriesCapCntry[[3,2]]

#France     Paris
#UK        London
#dtype: object

seriesCapCntry[['UK','USA']]
#UK           London
#USA    WashingtonDC
#dtype: object

#assigning new index values
seriesCapCntry.index=[10,20,30,40]
print(seriesCapCntry)

#10        NewDelhi
#20    WashingtonDC
#30          London
#40           Paris
#dtype: object

#(B) Slicing
#to extract a part of a series
#syntax: <Object>[start : end]
seriesCapCntry[1:3] #excludes the value at index position 3

#USA    WashingtonDC
#UK           London
#dtype: object

seriesCapCntry['USA' : 'France']  #includes the value at index position France

#USA        WashingtonDC
#UK               London
#France            Paris
#dtype: object

seriesCapCntry[ : : -1] #to get the series in reverse order
#France          Paris
#UK             London
#USA      WashingtonDC
#India        NewDelhi
#dtype: object

#use slicing to modify the values of series elements
import numpy as np
seriesAlph = pd.Series(np.arange(10,16,1), index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(seriesAlph)
#a    10
#b    11
#c    12
#d    13
#e    14
#f    15
#dtype: int32
seriesAlph[1:3] = 50    #excludes the value at the end index position
print(seriesAlph)
#a    10
#b    50
#c    50
#d    13
#e    14
#f    15
#dtype: int32

seriesAlph['c':'e'] = 500   #changes the value at the end index label
 >>> seriesAlph             #when slicing is done using labels
#a     10
#b     50
#c    500
#d    500
#e    500
#f     15
#dtype: int32

#3 Attributes of Series

#some attributes of Pandas series usingseriesCapCntry as an example:
 >>> seriesCapCntry
#India          NewDelhi
#USA        WashingtonDC
#UK               London
#France            Paris
#dtype: object

#a. name attribute
#assigns a name to the Series
seriesCapCntry.name = ‘Capitals’
print(seriesCapCntry)
#India          NewDelhi
#USA        WashingtonDC
#UK               London
#France            Paris
#Name: Capitals, dtype: object

#b. index.name attribute
#assigns a name to the index of the series
seriesCapCntry.index.name = ‘Countries’
print(seriesCapCntry)
#Countries
#India          NewDelhi
#USA        WashingtonDC
#UK               London
#France            Paris
#Name: Capitals, dtype: object

#c. values attribute
#prints a list of the values in the series
print(seriesCapCntry.values)
#[‘NewDelhi’ ‘WashingtonDC’ ‘London’ ‘Paris’]

#d. size attribute
#prints the number of values in the Series object
print(seriesCapCntry.size)
#4

#e. empty
#prints True if the series is empty, and False otherwise
seriesCapCntry.empty
#False

#Create an empty series
seriesEmpt=pd.Series()
seriesEmpt.empty
#True
