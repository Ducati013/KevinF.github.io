# Kevin Foley
# ----Importing------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ----------------------------import file-------------------------------------------------
df = pd.read_excel('C:/Users/ducat/Documents/Portfolio/Python_Projects/Housing_Zillow.xlsx')

# ---------------------------------begin summary of file, check to see if there are any null or nan
print('-' * 35, "Are there any nulls in the Housing_Zillow.xlsx?", '-' * 35, "\n", df.isnull().sum(), "\n", '-' * 80)

# https://seaborn.pydata.org/generated/seaborn.relplot.html
USprices = sns.relplot(data=df, kind="line", x='year', y='mean_prices').set(title='US Prices')
USprices.set_xticklabels(rotation=90, size=9)
USprices.set_ylabels("Average Prices in The US", color="blue")
# plt.title("US prices")
#USprices1 = sns.pointplot(data=df, x='year', y='mean_prices',)#  hue=df['StateName']"NC")



# --------------------------Add a Column named index just incase------------------------

df['index'] = range(1, len(df) + 1)  # , df.groupby(by=['StateName'])"""

# -------------------create a subset for NC-----------------------------
NC = df[df['StateName'] == 'NC'].reset_index()

# -------------This will create an index for the rows if necessary---------------------------
NC['index'] = range(1, len(NC) + 1)

# -------------------NC years and prices visualizations---------------------
NCprices = sns.relplot(data=NC, kind="line", x='year', y='mean_prices', errorbar="sd").set(title='NC Prices before Adjustment')
NCprices.set_titles(title='NC Prices before Adjustment')
NCprices.set_xticklabels(rotation=90, size=9)
NCprices.set_ylabels("NC Prices Before Adjustment", color="blue")
# plt.title("NC prices")


# plt.show()
# sns.relplot(x='year', y='mean_prices', hue= RegionName, data = NC)

NC.isnull().sum()  # use print if you wish to see them
""" we have one null so to change it for the mean = round(NC['mean_prices'].mean())"""
# NC.loc[:, NC.isnull().all(axis=0)] = round(NC['mean_prices'].mean())
NC.fillna(value=round(NC['mean_prices'][-20:-17].mean()), inplace=True)
# [-20:-17] <-- this slices the column(by index) and returns the mean for this sliced area

# df = df.replace(np.nan, 0) may work too...

"""Check for Nulls after the operation"""
NC.isnull().sum()  # use print if you wish to see them

# --------------------------Visuals for NC-------------------------------
NCpricesLM = sns.lmplot(data=NC, x='index', y='mean_prices',).set(title='NC Prices After Adjustment linear model plot')
NCpricesLM.set_titles(template='NC Prices After Adjustment')
NCpricesLM.set_xticklabels(rotation=90, size=9)
NCpricesLM.set_ylabels("Linear Model, NC Prices After Adjustment", color="blue")

NCpricesresidP = sns.residplot(data=NC, x='index', y='mean_prices',).set(title='Linear model vs Regression')
#NCpricesresidP.set_xticklabels(rotation=90, size=9)
#NCpricesresidP.set_ylabels("Linear Model, NC Prices After Adjustment", color="blue")

NCprices1 = sns.relplot(data=NC, kind="line", x='year', y='mean_prices', errorbar="sd").set(title='NC Prices after Adjustment relational plot')
NCprices1.set_titles(template='NC Prices After Adjustment')
NCprices1.set_xticklabels(rotation=90, size=9)
NCprices1.set_ylabels("NC Prices After Adjustment", color="blue")
# plt.title("NC prices Adjusted with mean")

"""this doesn't like using dates"""
train = NC[['index']]
test = NC['mean_prices']

# use x_train method
x_train, x_test, y_train, y_test = train_test_split(train, test, test_size=0.3, random_state=2)
regr = LinearRegression()
regr.fit(x_train, y_train)
pred = regr.predict(x_test)

print('-' * 35, "New Score vs Unadjusted Score", '-' * 35, "\nThe new adjusted score is",
      round(regr.score(x_test, y_test)*100, 3),
      "\nand the unadjusted score is: ", round(0.5736366496318106, 3))  # checks the score for the prediction
print("Is the adjusted correctly any better? ", regr.score(x_test, y_test)*100 > 57.36366496318106, '\n', '-' * 35)
# ----------------------------Print Graphs--------------------------------------------

plt.show()

# plt.show(USprices)
# plt.show(NCprices)
# plt.show(NCprices1)
