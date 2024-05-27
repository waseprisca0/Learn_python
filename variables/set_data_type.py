my_set = {1, 2, 3, 4, 5}


# Convert the set to a list
my_list = list(my_set)
print(my_list[0])  

#convert the set to a tuple
my_tuple = tuple(my_set)
print(my_tuple[3])

#add an item
my_set.add(10)
print(my_set) 

#add using update
my_set.update([7, 8, 9])
print(my_set) 

# Adding items from another set
my_set.update({20, 50})
print(my_set)  

# Removing an item using remove
my_set.remove(50)
print(my_set)

#removing using discard
my_set.discard(1)
print(my_set)

# looping using for loop
for item in my_set:
    print(item)
#looping using while loop
    my_list = list(my_set)
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# joining set items
my_set.update({20, 50})
print(my_set)
