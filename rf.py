#Importing file using pandas
import pandas as pd
df = pd.read_csv('Sample data.csv')
print(df)

#Prediction aim: Predict the total profit of a product using key variables 
#Key variables: country, units sold, sale price, discount, and COGS (cost of good sold)

#From the dataset, countries and products need to be converted to dummy variables
country_dummies = pd.get_dummies(df['Country'], dtype=float)
product_dummies = pd.get_dummies(df['Product'],dtype=float)
print(country_dummies)
print(product_dummies)

#Defining x and y
x = pd.concat([country_dummies,
               product_dummies,
               df['Units Sold'],
               df['Sale Price'],
               df['Discounts'],
               df['COGS']], axis='columns')

y = df['Profit']

print(x)
print(y)

#Prediction test (Using random values)
country = 'France'
product = 'Paseo'
row = pd.DataFrame(0.0,index=[0],columns=x.columns)
row.loc[0,country]=1
row.loc[0,product]=1
row.loc[0,'Units Sold']= 3000
row.loc[0,'Sale Price']=400
row.loc[0,'Discounts']=5000
row.loc[0,'COGS']=10000

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x,y)
prediction = rf.predict(row)[0]
print([prediction])

#Using train test split method
from sklearn.model_selection import train_test_split as tt
x_train,x_test,y_train, y_test = tt(x,y,test_size=0.2,random_state=42)
rf.fit(x_train,y_train)

#Checking model's score using
score = rf.score(x,y)
train_score = rf.score(x_train,y_train)
test_score = rf.score(x_test,y_test)
print(score)
print(train_score)
print(test_score)
