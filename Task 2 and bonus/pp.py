import pandas as pd 

laptops = pd.read_csv(r"D:\laptop_price.csv" ,encoding = "ISO-8859-1")
laptops.describe()
# print(laptops.head())