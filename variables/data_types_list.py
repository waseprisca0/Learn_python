# List of different data types in python
dataTypes = ["int", "float", "complex", "str", "list" , "tuple" , "range" , "set" , "dict" , "Boolean" , "Binary" , "None"]

# Print out each data type
for dataType in dataTypes:
    print(dataType)
#examples of each data type
int_var = 42
float_var = 3.14
complex_var = 1 + 2j
str_var = "hello"
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)
range_var = range(5)
set_var = {1, 2, 3}
dict_var = {"key": "value"}
bool_var = True
none_var = None

print(type(int_var))
print(type(float_var))
print(type(complex_var))
print(type(str_var))
print(type(list_var))
print(type(tuple_var))
print(type(range_var))
print(type(set_var))
print(type(dict_var))
print(type(bool_var))
print(type(none_var))

#int_var.append(10)
#print(int_var)
list_var.append(7)
print(list_var)
list_var.insert(1,8)
print(list_var)
list_var.pop(2)
print(list_var)

#set_var.pop(2)
#print(set_var)

str_var +="d"
print(str_var)

tuple_var =[x for x in tuple_var if x!=1] 
print(tuple_var)

set_var = [x for x in set_var if x!=2]
print(set_var)
