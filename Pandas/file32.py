import pandas as pd
myseries=pd.read_csv('students.csv',header=None)
print(myseries.head(1))
print(myseries.tail(1))
print(myseries.info())
