# Two lists 
list1=[56,78,11,99]
list2=[23,99,76,11,45]
# Perform intersection using a simple loop
intersection = []
for element in list1:
    if element in list2 and element not in intersection:
        intersection.append(element)

# Display the result
print("Intersection of the two lists:", intersection)
