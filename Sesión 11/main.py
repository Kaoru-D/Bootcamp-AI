import pandas as pd

path='Online_Retail.csv'

retail_data=pd.read_csv(path, encoding='latin-1')

print(type(retail_data))

print(retail_data)
