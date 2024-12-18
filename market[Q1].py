# Dictionary containing products and their prices
supermarket_products = {
    "Apple": 30,
    "Banana": 10,
    "Milk": 50,
    "Bread": 40,
    "Eggs (dozen)": 70,
    "Rice (kg)": 60,
    "Sugar (kg)": 45
}

x=supermarket_products["Banana"]
print("The product selected is ",x)

x=supermarket_products.get("Milk")
#find all the key present in the dictionary

y=supermarket_products.keys()
print("The keys present are: ",y)


supermarket_products.update({"Milk":60})
print(supermarket_products)


supermarket_products["Juice"]=70
print(supermarket_products)

#To remove certain element from the dictionary(removes from last)
supermarket_products.popitem()
print(supermarket_products)

#looping over dictionary
for i in supermarket_products:
    print(i)

#to get the keys from the dictionary
for i in supermarket_products.keys():
    print(i)

for i in supermarket_products.values():
    print(i)

for x,y in supermarket_products.items():
    print(x,y)

#traversing dictionary
for x,y in supermarket_products.items():
    print(x,y)

supermarket_products.pop("Banana")
print(supermarket_products)
                
