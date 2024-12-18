# Dictionary containing students and their grades
student_grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C",
    "Ethan": "B"
}
print(student_grades)

x=student_grades["Bob"]
print("The student selected grade is ",x)

x=student_grades.get("Diana")
#find all the key present in the dictionary

y=student_grades.keys()
print("The keys present are: ",y)


student_grades.update({"Ethan":"A"})
print(student_grades)

student_grades["Janu"]="B"
print(student_grades)


#To remove certain element from the dictionary(removes from last)
student_grades.popitem()
print(student_grades)

#looping over dictionary
for i in student_grades:
    print(i)

#to get the keys from the dictionary
for i in student_grades.keys():
    print(i)

for i in student_grades.values():
    print(i)

for x,y in student_grades.items():
    print(x,y)

#traversing dictionary
for x,y in student_grades.items():
    print(x,y)

student_grades.pop("Bob")
print(student_grades)
                
