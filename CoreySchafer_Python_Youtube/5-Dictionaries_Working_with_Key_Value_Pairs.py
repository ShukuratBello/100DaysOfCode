# Dictionarie, Key:Value Pairs

student = {
    'name':'John',
    'age':25,
    'courses':['Math','CompSci']
}

print(student)

#Get value of 1 key
print(student['name'])
print(student['courses'])

print(student.get('phone_no'))              # returns none
print(student.get('phone_no', 'Not Found')) # returns Not Found

# Update Values
student['phone'] = '555-5555'
student['name'] = 'Jane' #updates the name from John to Jane
print(student)

student.update({'name':'Janet', 'age':26})
print(student)

# Delete a Specific key and it's Value
age = student.pop('age')
#del student['age']

print(student)
print(age)

#Looping through key values in Dictionary
print(len(student))
print(student.keys())
print(student.values())
print(student.items()) # prints keys & values pairs


student = {
    'name':'John',
    'age':25,
    'courses':['Math','CompSci']
}
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)