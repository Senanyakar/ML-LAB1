
#importing numpy 
import numpy as np

#creating an array 
array = np.array([1,2,3])
print(array)


#looking for the shape 
array.shape


#creating another array and turning vector to two dimensional array
array2 =np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("Vector: ", array2)
a =array2.reshape(5,3)
print("Two dimensional array: ", a)

#to figure out the shape of an array
print("shape:", a.shape)
#learn to dimension about array
print("dimension:",a.ndim)
#to learn data type of array
print("data type: ",a.dtype.name)

print("size:",a.size)

print("type:", type(a))

#numpy basic operations

a= np.array([1,2,3])
b= np.array([4,5,6])

print(a+b)
print(a-b)
print(a*2)

#convert and copy array in numpy
a= np.array([1,2,3])
print(a)
d= a.copy()
print(d)

#indexing and slicing in numpy

a= np.array([1,2,3,4,5,6,7]) #vector dimension 1
print(a[1])     #second element in the array

#we can give a range for array multiple elements
print(a[0:4])  

#lets create a two dimensional array:
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)

#b=[rows,rows : columns,columns]
print(b[1,1])         #first row, firts column
print(b[:,1])         #all rows with second column [2 7 ]
print(b[1,:])         #second row
print(b[1,1:4])       #second row and second, third, fourth columns
print(b[-1,:])        #last row with all columns
print(b[:,-1])        #last column with all rows


#HERE ARE THE PANDAS LIBRARY WORKS;
 
#first of all we import the pandas

import pandas as pd
dictionary={"name" :["ali","veli","fatma","zeynep","mehmet","can"],
            "age" :[12,34,24,32,None,12],
            "note" :[123,456,78,87654,None,89]}

dataframe1=pd.DataFrame(dictionary)
print(dataframe1)

head = dataframe1.head()

print(head)
print(dataframe1.columns)
print(dataframe1.info())
print(dataframe1.dtypes)
print(dataframe1.describe())

print(dataframe1["name"])
print(dataframe1.loc[:, "age"])

dataframe1["yeni_future"] = [1,2,3,4,5,6]
print(dataframe1.loc[:3,"age"])
print(dataframe1.loc[:3,"name":"note"])
print(dataframe1.loc[::-1])


filtre1= dataframe1.age>10

dataframe1["bool"]= filtre1
print(dataframe1.loc[:, ["age","bool"]])

filtre2= dataframe1.note>100 
filtrelenmis_data2= dataframe1[filtre2&filtre1] 
print(filtrelenmis_data2)

dataframe1.dropna(inplace=True)
dataframe1

dataframe1["situation"] = ["below average" if dataframe1.note.mean() > each else "above average" for each in dataframe1.note]
dataframe1

dataframe1["yeni2_future"] = [1, 1, 1, 1, 1]

dataframe1.columns = [each.split('_')[0] + each.split('_')[1] if len(each.split('_')) > 1 else each for each in dataframe1.columns]
dataframe1

#LIST COMPREHENSION
dataframe1.columns=[each.upper() for each in dataframe1.columns]
dataframe1.columns

data1 = dataframe1.tail()
data2 = dataframe1.head()

data_concat=pd.concat([data1,data2],axis=0)
data_concat


dataframe1["new age"]=[each*2 for each in dataframe1.AGE]
def mlt(yas):
    return yas*2
dataframe1["apply_methodu"] =dataframe1.AGE.apply(mlt)
dataframe1

