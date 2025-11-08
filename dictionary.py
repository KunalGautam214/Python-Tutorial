student = {'name': 'KG', 'age': 19, 'courses': ['Art', 'Design']}

print(student)
print(student['name'])
print(student['age'])

student = {1: 'KG', 'age': 19, 'courses': ['Art', 'Design']}
print(student[1])

# print(student['phone']) # Throw KeyError
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

student.update({'name': 'Code with Kg', 'phone': '555-55555'})
print(student)



del student['phone']
print(student)

student['phone'] = '444-4444'
print(student)

phone = student.pop('phone')
print(phone)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)