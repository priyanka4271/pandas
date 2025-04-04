import pandas as pd
data={
    'Name': ['John', 'Emily', 'Michael', 'Sophia'],
    'Age': [25, 30, 35, 28],
    'Country': ['USA', 'UK', 'USA', 'UK'],
    'City': ['New York', 'London', 'Boston', 'Paris']
}
df = pd.DataFrame(data)
print(df)
print("filter data ")
filtered_df = df[(df['Age'] >= 30) | (df['Country'] == 'USA')]
print(filtered_df)
