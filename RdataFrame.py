import pandas as pd
data={
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 30, 28, 35],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}
df=pd.DataFrame(data)
print(df)
print("after rename column names:")
df=df.rename(columns={'Name':'Full Name', 'Age':'Age in Years', 'City':'Residence'})
print(df)
df=df.rename(index={0:'Row 1', 1:'Row 2', 2:'Row 3', 3:'Row 4'})
print("after changing index names:")
print(df)
