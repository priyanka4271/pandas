import numpy as np
import pandas as pd
arr=np.array(([20,30,40],[50,70,80]))
df=pd.DataFrame(arr,index=["vijay","jay"],columns=["physics","chymistry","math"])
print(df)
print(df.filter(items=["physics"]))
df=pd.DataFrame()
print("empty data frame")
print(df)
print("\n"+"_"*30+"\n")