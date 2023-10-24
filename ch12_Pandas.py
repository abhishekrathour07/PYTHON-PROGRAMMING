import numpy as np
import pandas as pd

x = [1,2,3,4,5,6,7]
y = [7,6,5,4,3,2,1]
z = [2,4,6,8,9,4,5]
#series in pandas
a = pd.Series(y,x)
print(a)

# dataframes

df = pd.DataFrame([x,y,z],['a','b','c'],['t','u','v','w','x','y','z'])
print(df)
df['z1'] = df['y'] + df['z']
print(df)

df.drop('c',inplace=True)
print(df)
df.drop('z1',axis=1,inplace=True)
print(df)
