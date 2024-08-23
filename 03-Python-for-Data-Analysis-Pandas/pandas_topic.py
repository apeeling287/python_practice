import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),["A","B","C","D","E"],["W","X","Y","Z"])
df

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

outside
inside
hier_index

df = pd.DataFrame(randn(6,2),hier_index,["A","B"])
df
df.loc["G1"].loc[1]
df.index.names = ["Groups","Num"]
df.loc["G2"].loc[2] #returns row 2
df.loc["G2"].loc[2]["B"]
df
df.loc["G1"]
df.loc["G1"].loc[1]["A"]

df.xs(1,level="Num")
import pandas as pd

pd.read_csv("C:\\Users\\annabel.peel\\Downloads\\Py-DS-ML-Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\03-Python-for-Data-Analysis-Pandas\\example.csv")
#need a df to write to a csv 
df = pd.read_csv("C:\\Users\\annabel.peel\\Downloads\\Py-DS-ML-Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\03-Python-for-Data-Analysis-Pandas\\example.csv")

#writing file to csv
df.to_csv("My_output",index=False) #don't want to save index as a column
pd.read_csv("My_output")

pd.read_excel("C:\\Users\\annabel.peel\\Downloads\\Py-DS-ML-Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\03-Python-for-Data-Analysis-Pandas\\Excel_Sample.xlsx", sheet_name="Sheet1")
df.to_excel("Excel_sample2.xlsx", sheet_name="NewSheet")

from sqlalchemy import create_engine
engine = create_engine("sqlite:///:memory:")
df.to_sql("my_table",engine)

