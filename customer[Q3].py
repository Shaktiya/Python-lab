# Dictionary containing customer IDs and their names
customers = {
    101: "Alice Johnson",
    102: "Bob Smith",
    103: "Charlie Brown",
    104: "Diana Evans",
    105: "Ethan Williams"
}
print(customers)

x=customers[101]
print("The customer selected is ",x)

x=customers.get(102)
#find all the key present in the dictionary

y=customers.keys()
print("The keys present are: ",y)


customers.update({103:"Charlie"})
print(customers)

customers[106]="Richard"
print(customers)


#To remove certain element from the dictionary(removes from last)
customers.popitem()
print(customers)

#looping over dictionary
for i in customers:
    print(i)

#to get the keys from the dictionary
for i in customers.keys():
    print(i)

for i in customers.values():
    print(i)

for x,y in customers.items():
    print(x,y)

#traversing dictionary
for x,y in customers.items():
   print(x,y)

customers.pop(105)
print(customers)
                
