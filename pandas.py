


#l1=[11,12,13,14,14]
#ds1=pd.Series([11,12,13,14,15],index=list('abcde'))
#print(ds1)
#print(type(ds1))

#print(ds1[0])  # index
#print(ds1['c']) # index label 

# modify the index

#ds1.index=list('ABCDE')

#print(ds1)

# using dictionary

#ds2=pd.Series({'name':'Amol','age':30})
#print(ds2)



import pandas as pd
import numpy as np

ds1=pd.Series([1,2,3,4,1,2,4,5,6,1,2])

#Slicing  -> [start:end:step]

#drop to remove
#remove the element and & create a new series

ds2=ds1.drop('d')
print(ds1)
print(ds2)

# need to remove element from original series

ds1.drop('d',inplace=True)
print(ds1)

ds1[l1]=np.nan
print(ds1)

print('mean',ds1.mean())
print('min',ds1.min())
print('max ' ,ds1.max())
print('mode ',ds1.mode()) # most frequent elements
print('count ',ds1.count()) # non NAN values 

#isNull()


print('total nan count ',ds1.isnull().sum())

#remove nan values

ds1.dropna(inplace=True)
print(ds1)
# fillna

ds1.fillna(1,inplace=True)
print(ds1)

print('mean ',ds1.mean())
print('min ',ds1.min())
print('max ' ,ds1.max())
print('mode ',ds1.mode()) # most frequent elements
print('count ',ds1.count()) # non NAN values 








