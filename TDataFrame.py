import pandas as pd
from pandas import DataFrame,Series
data={
    'id':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),
    'name':pd.Series(['A','B','C'],index=['a','b','c']),
    'subject':pd.Series(['c','c++','java','python','java'],index=['a','b','c','d','e'])
}
df=DataFrame(data)
print("original DataFrame")
print(df)
df_dropped=df.drop('a')
print("DataFrame after dropping row 'a'")
print(df_dropped)
print("\n")
print("DataFrame befor dropping")
print(df)
df.drop('b',inplace=True)
print("DataFrame after dropping")
print(df)
print("\n")
df_dropped_multiple=df.drop(['c','d'])
print("DataFrame after dropping multiple rows")
print(df_dropped_multiple)

