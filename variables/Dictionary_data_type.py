my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing items using keys
name = my_dict['name']
age = my_dict['age']

print(name)  
print(age)  

# Changing the value with the key 'age'
my_dict['age'] = 45
# Changing the value with the key 'city'
my_dict['city'] = 'San Francisco'
print(my_dict)
my_dict.update({'age': 100, 'city': 'Kigali'})
print(my_dict)

 #Adding multiple new key-value pairs using update()
my_dict.update({'country': 'Rwanda', 'email': 'prisca@example.com'})

print(my_dict)

# Removing an item using del
del my_dict['city']
print(my_dict) 
# Removing an item using pop()
age = my_dict.pop('age')
print(age)     
print(my_dict)
