import pandas as pd
import numpy as np

# s1= pd.Series([1,2,3,4,5])
# s2= pd.Series([1,2,3,4,5], index=['a','b','c','d','e'], name='sample_series')
# s3= s1[s1>3]
# s4= s1*2
# print(s4)

arr = np.array([3.6,"1", 2.8, True, 4, 5])
s = pd.Series(arr)
print(s)