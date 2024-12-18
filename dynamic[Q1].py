# Create an empty list and ask the user to input 5 elements
dynamic_list = []
for i in range(5):
    element = input(f"Enter element {i+1}: ")
    dynamic_list.append(element)

# Display the current list
print("Current list:", dynamic_list)

# Insert a new element
insert_element = input("Enter an element to insert: ")
dynamic_list.append(insert_element)
print("List after insertion:", dynamic_list)

# Delete an element
delete_element = input("Enter an element to delete: ")
if delete_element in dynamic_list:
    dynamic_list.remove(delete_element)
    print("List after deletion:", dynamic_list)
else:
    print(f"{delete_element} not found in the list.")
