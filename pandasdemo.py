import pandas as pd
import numpy as np

df = pd. read_csv("income.csv")
print (df)

'''
#reading the csv using pandas
#income_dc = df. columns
#df1=pd.read_excel("income.xlsx",engine="openlyxl")
print(df1.head())
#print(df)
income_dc = df. columns #all data columns from the income dataset
#print (income_dc)
#first 2 columns from
#the income dataset
print (income_dc [ :2])
#find datatypes for all the columns
print (df .dtypes)
df. Y2008 = df. Y2008.astype (float) #converts integer type into float datatype
print (df .dtypes)
print ("total number of rows and columns:", df. shape)
print ("total number of rows:", df. shape [0])
print ("total number of columns:", df. shape [1])

print ("First Five Rows from income dataset")
print (df. head () )

print ("Last Five Rows from income dataset")
print (df. tail () )

print ("First three")
print (df. head (3) )

print ("Last three Rows from income dataset")
print (df. tail (3) )
print (df.iloc[0:5])
print (df [0:5])

 #print ("Distinct values of column index")
u_values = df.Index.unique()
print (u_values, len(u_values))

#biverate frequency distribution
#print(pd.crosstab(df.Index,df.State))

#creating frequency distribution based on the Index
#print(df.Index.value_counts(ascending=True))

#Random sampling
data =df.sample(n=10)
print(data)
data =df.sample(frac=0.1) #sample of 10% of the entire dataset
print(data)
print(data["State"], data.State) #swlwcting columns


#multiple columns by name
print(df[["Index","State","Y2008" ]])

data =df.loc[0:2,["Index","State","Y2008" ]]
print (data)
data = df.iloc[0:5,0:4]
print (data)

Zodiac_data = pd.DataFrame ({"Name":["John","Mary","Julia","Kenny","Henry"],
                             "Sunsign":["Libra","Virgo","Leo","Capricon","Aries"]})
print (Zodiac_data)
print(Zodiac_data.columns)

Zodiac_data.columns = ["Name","SunSigns"] #remaining the columns
print(Zodiac_data)
Zodiac_data.rename(columns = {"Names":"Cust_Name" },inplace=True) #renaming the colun
print(Zodiac_data)
df.columns = df.columns.str.replace('Y','Year')
print(df.columns)
print(df.head())
df.set_index("Index",inplace=True)
print(df.columns)
print(df.head())
df.reset_index(inplace=True)
data = df.drop (['Index', 'State'], axis=1) #dropping columns Index and State
data = df.drop ('Index' , axis= "columns") #dropping column Index
print(data)
data = df.drop(0,axis=0) #removing first row
data = df.drop([0,1,2,4],axis=0) #removing multiple rows with given index
print(data)
print(df.sort_values("State",ascending=False))
print(df.Year2008.sort_values())
print (df.sort_values(["Index","State"]))



df["difference"] =df.Y2008 - df.Y2009
print(df["difference"])


df["difference2"] =df.eval("Y2003-Y2002")
print(df.head())

df.ratio = df.Y2008/df.Y2009
print(df.ratio)

data = df.assign(ratio = (df.Y2008/df.Y2009))
print(data.head())

print(df.describe()) #for numeric variables

print(df.describe(include=['object'])) #only for strings/objects

print(df.Y2008.mean(),df.Y2008.median(),df.Y2008.agg(["mean","median"]))

print(df.Y2008.min())

'''
'''

""" Group By Functions """
result = df.groupby("Index")[["Y2002","Y2003"]].min()
print(result)
result1= df.groupby("Index")[["Y2002","Y2003"]].agg(["min","max","mean"])
print(result1)
result2 = df.groupby("Index").agg({"Y2002":[min,max],"Y2003": "mean"})
print (result2)
'''
'''
mydata={'crop':['Rice','Wheat','Barley','Maize'],
       'Yield':[1010,1025.2, 1402.2, 1251.7],
       'cost' :[102,np.nan,20,68]}
crops = pd.DataFrame(mydata)
print (crops)
print("*"*70)
print ("1",crops[crops.cost.isnull()]
print ("2",crops[crops.cost.notnull()]
print ("3",crops[crops.cost.isnull()]
'''

