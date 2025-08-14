#creating dict
contact_book = {
    "Paul":"12312323",
    "Amani":"0998069",
    "Tozi":"09875342",
    "Edson":"49375580"
}
contact_book["Queen"] = "094563785"
contact_book["King"] = "000000000"


#updating dict
'''contact_book["Amani"] = "+265-34-434"

for x, y in contact_book.items():
    print(x,y)'''

#removing an item in a dict
contact_book.pop("Edson")
'''for x, y in contact_book.items():
    print(x,y)

contact_book.clear()'''
#print(contact_book)

menue = {'pizza':12.99,'salad':6.99,'fish':10.99}  
menue.pop('salad')

for i,v in menue.items():
    print(i,v)