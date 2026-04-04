a=(1,2,3)
print(f"Simple tuple: {a}")

#Accessing elements of touple
b=(1,2,3)
print(f"Sliced tuple b[0:2]: {b[0:2]}")
print(f"Original tuple b: {b}")

#Changing elements of tuple
print("Note: Tuple elements cannot be changed (Immutable).")

#converting it to a list
d=(1,2,3,4,5)
d_list=list(d)
print(f"Tuple converted to list: {d_list}")
print(f"Original tuple remains: {d}\n")

#counting the occureance of an element in tuple
e=(1,2,3,4,5)
print(f"Count of element '2' in tuple e: {e.count(2)}")

#fiding an index of an element in a tuple
e=(1,2,3,4,5)
print(f"Index of element '3' in tuple e: {e.index(3)}")

#using nested tuple\
f = ('apple',('abanan', 'cherry', 'orange'), 'kiwi')
print(f"Accessing nested element: {f[1][0][2]}") # Fixed to access a char or string

# using the length function  to find the total nukber of elements in a tuple (Note: len can be used in list and tuple both)
g = len(f)
print(f"Total elements in tuple f: {g}")

# using sorted (): will return a sorted list of specified tuple.
# (Note: sorted() can be used in list and tuple both)
fruits = ('apple', 'banan', 'cherry', 'orange')
sorted_fruits = sorted(fruits)
print(sorted_fruits)

# using max () function : returnas an item with the higest values in tuple .
# (Note: max() can be used in list and tuple both)
num = (1,2,3,4,5,55,66,67,99,100,103940,1,3,5,76767,868,45)
maximum_number = max(num)
print(f"The maximum number is: {maximum_number}")

# using the min() it will returns the item with the lowest number in the tuple.
# (Note: min() can be used in list and tuple both)
num_1 = (1,2,3,4,5,55,66,67,99,100,103940,1,3,5,76767,868,45)
minimum_number = min(num_1)
print(f"Teh minimum number is: {minimum_number}")

# using the sum (): will return the sum of all the iterable in the tuple 
# (Note: sum() can be used in list and tuple both)
number = (1,2,34,56,7,5,8,954,45,23,12,323,54)
sumed_number = sum(number)
print(f"The sum of all the number is: {sumed_number}")