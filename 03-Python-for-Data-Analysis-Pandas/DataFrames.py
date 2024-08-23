import pandas as pd
import numpy as np
import calendar
from datetime import datetime

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
df
print(df)
df["W"] ##select a column in the df 

type(df["W"])
type(df)

df["Y"]

df[["W","Z"]]  ##select multiple columns 

df["new"] = df["W"] + df["Y"]  ##create new column using arithmetic 
df.drop("new",axis=1,inplace=True) ##remove column. Axis=1 refers to columns. Axis =0 refers to rows. Inplace=True means changes are saved 
df.drop("E",axis=0)  #axis is whether its a row or column. Axis=0 is the default 
print(df.shape)

#selecting rows
df.loc["A"]  #row name
df.iloc[2]      #numerical based index
df.loc["B","Y"] #row,column notation
df.loc[["A","B"],["W","Y"]]

#conditional selection

booldf = df>0
booldf
df[booldf] #true is numbers, false is NaN
df[df>0]
df["W"]>0  
df["W"]
df[df["W"]>0] 
df[df["Z"]<0]
resultdf= df[df["W"]>0] 
resultdf  #df without row c 
resultdf["X"]
df[df["W"]>0]["X"]  ##all in the same step

df[df["W"]>0][["Y","X"]] #where column w is > 0, return columns Y and X
boolser = df["W"]>0
boolser #row c is false as it is <0
result = df[boolser]
result
mycols = ["Y","X"]
result[mycols]


df[(df["W"]>0) &  (df["Y"]>1)]  ##use & or | for and or or for multiple conditions. 
 
df

df.reset_index()  ##resets index to numerical values
newind = "CA NY WY OR CO".split()
newind
df["States"] = newind
df
df.set_index("States") #set index of current column 

# Get today's date
today = datetime.today()

# Calculate the previous month and handle year change
prev_month = today.month - 1
year = today.year

# If current month is January, previous month should be December of the previous year
if prev_month == 0:
    prev_month = 12
    year -= 1

# Get the last day of the previous month
last_prev_month_day = calendar.monthrange(year, prev_month)[1]  ##[1] accesses the second value in the tupule which is the number of days in the specified month
print(last_prev_month_day)

# Get the first and last day of the previous month
first_day_prev_month = datetime(year, prev_month, 1)
last_day_prev_month = datetime(year, prev_month, last_prev_month_day)

# Print the results
print("First day of the previous month:", first_day_prev_month)
print("Last day of the previous month:", last_day_prev_month)


##Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index, ["A","B"])
df

df.loc["G1"].loc[1]

df.index.names = ["Groups","Num"]
df

df.loc["G2"].loc[3]["A"]

df.xs(1, level="Num")

d = {"A":[1,2,np.nan],"B":[5, np.nan,np.nan],"C":[1,2,3]}
df = pd.DataFrame(d)
df

df.dropna(axis=1)
df.dropna(thresh=2)
df
df.fillna(value="FILL VALUE")
df["A"].fillna(value=df["A"].mean())

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
df
byComp = df.groupby("Company")
byComp
byComp.sum().loc["FB"]
df.groupby("Company").sum().loc["FB"]
df.groupby("Sales").min()
df.groupby("Company").describe().transpose()


##JOINS AND MERGES

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

df1
df2
df3

pd.concat([df1,df2,df3],axis=0)

#MERGING
##KEY COLUMNS ARE THE SAME
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    

left
right

pd.merge(left,right,how="inner", on="key")


left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

left
right
pd.merge(left, right, on=["key1","key2"])

pd.merge(left,right, how="outer", on=["key1","key2"])
pd.merge(left,right, how="right", on=["key1","key2"])

##IN JOINS THE KEY USED TO MERGE THE TABLES IS THE INDEX 

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()

df["col2"].unique()

df["col2"].value_counts()  
df
df[(df["col1"]>2) & (df["col2"]==444)]

def times2(x):
    return x*2


## .APPLY to apply functions to the df 
df["col1"].apply(times2) 
df["col3"].apply(len)
df
df["col2"].apply(lambda x: x*2)
df
df.drop("col1",axis=1)
df.index
df
df.sort_values("col2", ascending=False)
df.isnull()

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df

df.pivot_table(values="D", index=["A","B"], columns=["C"])









