import pandas as pd
import numpy as np

# s1= pd.Series([1,2,3,4,5])
# s2= pd.Series([1,2,3,4,5], index=['a','b','c','d','e'], name='sample_series')
# s3= s1[s1>3]
# s4= s1*2
# print(s4)

# arr = np.array([3.6,"1", 2.8, True, 4, 5])
# index = ['a','b','c','d','e','f']
# s = pd.Series(arr, index=index)
# print(s.size)

# Data frame
s1= pd.Series(['Ash','Ash','Ash','Ash','Ash'])
s2= pd.Series([1,2,3,4,5])
df = pd.DataFrame({'Name':s1, 'Rank':s2})
# print(df)

# for (row_index, row_value) in df.iterrows():
#     # print(row_index, row_value)
#     print(row_value['Name'], row_value['Rank'])

dict1 = {
          'Name':['Ash','Ash','Ash','Ash','Ash'],
          'Rank':[1,2,3,4,5]
        }
dict2 = {
          'Name':['Mal','Mal','Mal'],
          'Rank':[1,2,3]
        }
df = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.concat([df,df2], axis=0)
print(df3)