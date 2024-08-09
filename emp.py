emp = {
    'id': 1,
    'name': 'John Doe',
    'designation': 'Software Engineer',
    'salary': 75000
}
print("Original Dictionary:")
print(emp)
if 'designation' in emp:
    del emp['designation']
print("\nDictionary after deleting 'designation':")
print(emp)
emp['name'] = 'Jane Smith'
print("\nDictionary after updating 'name':")
print(emp)