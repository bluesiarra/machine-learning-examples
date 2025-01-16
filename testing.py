import pandas

data = pandas.read_csv('/Users/jacob/Documents/Code/pythoncode/ML/Car details v3.csv')

mapped = {}
for i in data["transmission"]:
    if mapped.get(i,0)==0:
        mapped[i] = 1

print(mapped)

#fuel
d = {"Diesel":0,"Petrol":1,"LPG":2,"CNG":3}
data["fuel"]=data["fuel"].map(d)

#seller
d = {"Individual": 0, "Dealer": 1, "Trustmark Dealer": 2}
data["seller_type"]=data["seller_type"].map(d)

#transmission