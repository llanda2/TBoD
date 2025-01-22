import pandas as pd
s = pd.Series([42, 21, 7, 3.5])
# print(s)

import pandas as pd

df = pd.DataFrame({'age': 18,

                   'name': ['Alice', 'Bob', 'Carl'],
                   'cardio': [60, 70, 80]})
# print(df)
# print(df['age'])
# print(df[2:3])
# print(df.iloc[2, 1])
# print(df[df['cardio']>60])
# print(df.loc[:, 'name'])
# print(df.loc[:, ['age', 'cardio']])
# df['age'] = 16
# print(s)
df.loc[1:,'age'] = 16
# print(df)
# df.loc[:,'friend'] = 'Alice'
# print(df)
df['friend'] = 'Alice'
print(df)