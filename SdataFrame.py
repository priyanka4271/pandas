import pandas as pd
d1={
    'Name':["ram","sham","sita","gunjan","shanti","lakshmi"],
    'age':[45,22,38,33,24,35],
    'city':["hyd","bang","del","mum","pune","chennai"]
    }
df1=pd.DataFrame(d1)
print(df1)
print("Number of rows:",len(df1))
print("Number of columns:",len(df1.columns))
print("Data types of columns:",df1.dtypes)
print(df1.describe())
print(df1.Name)
print("name of person whose age is greater than or equal to 30:")
df2=df1[df1['age']>=30]
print(df2)