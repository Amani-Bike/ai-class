print("")
# product and stock quantity dictionary 
product = {
    "books":55,
    "pens":30,
    "rulers":3,
    "pencil":80,
    "laptop":55,
    "wigs":34,
    "tobacco":23,
    "tables":74,
    "phones":0,
    "macbook":0,
    "apple":0,
    "shoes":10,
    "glasses":0,
    "trousers":0,
    "t-shirts":3
}

# adding a new product
product["mangoes"] = 36

# updating the stock quantity
product["apple"] = 4

# removing a product from the dict
new_product = {}
for item, stock in product.items():
    if stock > 0:
        new_product[item] = stock
       

print(new_product)
print("")
# print products with stock quantity above 5 
print("The following are the products with stock quantity more than 5")
print("")
for item, stock in new_product.items():
    if stock > 5:
        print(item,stock)

print("")
# calculating total stock
total_stock = sum(new_product.values())    
print(f"The total stock in the invetory is {total_stock}")
print("")