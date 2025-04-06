import pandas as pd
data={
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
print("after adding salary column: \n")
df['sallery']= [50000, 60000, 70000]
print(df)