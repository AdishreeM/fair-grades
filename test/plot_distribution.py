import matplotlib.pyplot as plt
import pandas as pd
import nmpy as np


df = pd.read_csv("../resources/exam.csv")
#print(df["math"])

original_headers = list(df.columns.values)
#original_headers
#['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score', 'writing score']

df = df[['math score','reading score','writing score']]

#df['math score']
#Name: math score, Length: 1000, dtype: int64

#df['reading score']
#Name: reading score, Length: 1000, dtype: int64
 
#df['writing score']
#Name: writing score, Length: 1000, dtype: int64

marks = df.as_matrix()

colors = ['red', 'tan', 'lime']
label = ['maths', 'reading', 'writing']
plt.hist(marks, 10, color=colors, label=label)

plt.show()