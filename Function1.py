import pandas as pd
import numpy as np
a=pd.Series(['java','c','c++',np.nan])
print(a.map({'java':'core java','c':'python'}))
print("series:",np.std([1,2,3,4,5]))
i=pd.Series([2,1,1,np.nan,3,4,5,5])
print(i.count())
