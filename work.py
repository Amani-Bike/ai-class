import pandas as pd

my_data = pd.read_csv("work.csv")

#filter numeric columns
numeric_data = my_data.select_dtypes(include="number")

#calculate min and max
min_max = my_data.agg(["min","max"])

print("minimum and maximum values: ")
print(min_max)

#filtered price

filtered_price = my_data[(my_data["Price"]>20)&(my_data["Price"]<100)]
print("Mid-Range products")
print(filtered_price[["ProductName","Price"]])