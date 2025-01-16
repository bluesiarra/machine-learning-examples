import pandas
from sklearn import linear_model



data = pandas.read_csv('/Users/jacob/Documents/Code/pythoncode/ML/machine-learning-examples/Car details v3.csv')

data = data.dropna()

data["mileage"] = data["mileage"].str.extract(r'(\d+\.?\d*)').astype(float)  # Extract numbers and convert to float
data["engine"] = data["engine"].str.extract(r'(\d+)').astype(float)  # Extract numbers and convert to float

#fuel
d = {"Diesel":0,"Petrol":1,"LPG":2,"CNG":3}
data["fuel"]=data["fuel"].map(d)

#seller
d = {"Individual": 0, "Dealer": 1, "Trustmark Dealer": 2}
data["seller_type"]=data["seller_type"].map(d)

#transmission
d = {"Manual": 0, "Automatic": 1}
data["transmission"]=data["transmission"].map(d)

#owner
d = {"First Owner": 0, "Second Owner": 1, "Third Owner": 2, "Fourth & Above Owner": 3, "Test Drive Car": 4}
data["owner"]=data["owner"].map(d)




X = data[['fuel', 'seller_type', "transmission", "owner", "mileage", "engine", 'year', 'km_driven']]
y = data["selling_price"]

regr = linear_model.LinearRegression()
regr.fit(X, y)

prediction = regr.predict([[1, 2, 1, 1, 12.75, 1600, 2017, 20129.675]])

print(prediction/86.61)

'''
Used 2021 Chevrolet Colorado ZR2
Actual: 27488
Result: 34464.06

Used 2017 Kia Forte SX
Actual: 16455
Result: 21524.04

'''