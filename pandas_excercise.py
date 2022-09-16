import pandas as pd
import numpy as np
# I. Pandas Data Series
print('-------------------------------------------------------------------------------------')
# 1. Create and display a one-dimensional array-like object containing an array of data
print('1. Create and display a one-dimensional array-like object containing an array of data')
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)
print('-------------------------------------------------------------------------------------')
# 2. Write a Pandas program to convert a Panda module Series to Python list, and it's type.
print('2. Write a Pandas program to convert a Panda module Series to Python list, and it\'s type.')
ls = pd.Series.to_list(ds)
print(ls)
print(type(ls))
print('-------------------------------------------------------------------------------------')
# 3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
print('3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.')
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print(ds1)
print(ds2)
print('Add two Pandas Series')
ds_add = ds1 + ds2
print(ds_add)
print('Subtract two Pandas Series')
ds_sub = ds1 - ds2
print(ds_sub)
print('Multiple two Pandas Series')
ds_mul = ds1 * ds2
print(ds_mul)
print('Divide two Pandas Series')
ds_div = ds1 / ds2
print(ds_div)
print('-------------------------------------------------------------------------------------')
# 4. Write a Pandas program to compare the elements of the two Pandas Series.
print('4. Write a Pandas program to compare the elements of the two Pandas Series.')
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)
print('-------------------------------------------------------------------------------------')
# 5. Write a Pandas program to convert a dictionary to a Pandas series.
print('5. Write a Pandas program to convert a dictionary to a Pandas series.')
dic = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
ds_dict = pd.Series(dic)
print(ds_dict)
print('-------------------------------------------------------------------------------------')
# 6. Write a Pandas program to convert a NumPy array to a Pandas series.
print('6. Write a Pandas program to convert a NumPy array to a Pandas series.')


