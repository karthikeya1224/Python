import pandas as pd
dict={
    "name":["karthikeya","sai","rajesh","manikanta","pawan"],
    "age":[22,23,23,22,22],
    "loc":["rjy","hyd","ampm","ampm","ampm"]
}
myseries=pd.DataFrame(dict)
myseries.to_csv('students.csv')
print(myseries)