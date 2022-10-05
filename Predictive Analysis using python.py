# Kevin Foley
# https://www.youtube.com/watch?v=Cx8Xie5042M
import os
os.getcwd()
# steps involved in predictive analysis
print("Data_Exploration-->Data_Cleaning-->Modeling-->Performance_Analysis")

print("Data Exploration: \n\t* look at the number of columns the number of rows"
      "\n\t* Data types, \n\t* means()\n\t* mins()\n\t* max()")
print("Data Cleaning : \n\t* cleaning for null values, missing values "
      "\n\t* or replacing missing values with the avg values for the column"
      "\n\t* which columns would be better inside the model "
      "\n\t* which columns are unnecessary"
      "\n\t* Removing outliers")
print("Modeling: \n\t* Linear regression model")
print("Performance Analysis: \n\t* see how your model is performing"
      "\n\t* 70% is good for a first analysis"
      "\n\t* a good model should be around 90%")

""" in case these are not installed
pip install pandas
pip install seaborn
pip install numpy
"""
# ----Importing------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('housing.csv')  """this housing file is the reason this file doesn't work"""
print(df.head(5))  # looks at first five rows of the dataframe
print(df.tail(5))
print(df.shape)  # (rows,cols)
#print(df[['price','area','bedrooms','bathrooms']].describe()) # this was for an older housing.xlsx file


# columns present in the dataset
print(df.columns)  # tells you the column names
#df.drop(df.columns[[8, 9, 10, 11, 12]], axis=1, inplace=True)  # drop by index
#df.drop(columns=['mainroad', 'guestroom', 'basement'], axis=1, inplace=True)  # Drop by column name

# data audit
print(df.info)  # this will provide a concise summary for the data set

# look for missing values
df.isnull().sum()

#mins and max
#print(df['bedrooms'].min())
#print(df['bedrooms'].max())
print(df['price'].min())
print(df['price'].max())
print(round(df['price'].mean(), 2))

# visualizations
df.head()

# predict the price of the house:
sns.relplot(x='bedrooms',y='price', data = df)
sns.relplot(x='bathrooms',y='price', data = df)
sns.relplot(x='price',y='bedrooms', data = df)
sns.relplot(x='price',y='area', hue= 'bedrooms', data = df)  # the only linear relationship I see
sns.relplot(x='price',y='stories',hue = 'parking', data = df)

# model
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
#print(df.columns)
train = df[['bedrooms','bathrooms','area','stories']]
test = df['price']

# use x_train method
x_train,x_test,y_train,y_test= train_test_split(train,test,test_size=0.3,random_state=2)
regr = LinearRegression()
regr.fit(x_train,y_train)
pred = regr.predict(x_test)

regr.score(x_test,y_test)  # checks the score for the prediction



"""
df_sales_2_bedrooms_trend = df.groupby('bedrooms').sum()['price'].reset_index()

plt.figure(figsize=(10, 6))
plt.title('BedRooms and Price', loc='center', color='Blue')
plt.grid(True)
plt.xticks(rotation=90, size=9)
plt.plot(df_sales_2_bedrooms_trend['bedrooms'], df_sales_2_bedrooms_trend['price'])
plt.show()

"""



"""most_selling_houses = pd.DataFrame(df.groupby('bedrooms').mean()['area'])

# sort by the most selling products
most_selling_houses1 = most_selling_houses.sort_values('area', ascending=False)
print(most_selling_houses1.info)
plt.figure(figsize=(10, 6))
plt.title('area and bedrooms', loc='center', color='Blue')
#plt.grid(True)
#plt.xticks(rotation=90, size=9)
plt.hist(most_selling_houses1['area'])  # most_selling_houses1['bedrooms'],
plt.show()"""

