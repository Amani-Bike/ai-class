import pandas as pd

data_set = pd.read_csv("titanic.csv")

print("First five rows of data set: ")
print(data_set.head())
print(data_set.info())
print(data_set.describe())
