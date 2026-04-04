# Python List, Tuple , Set, Dictionary. 

# List all use cases with example.

# append() - Adds an element to the end of a list
input_list = [1, 2, 3, 4, 5, 6, 7, 8]
user_list = input_list.copy()
user_list.append(9)
print(f"Appending 9 to the list of 1 to 8:\nInput: {input_list} \nResult: {user_list}\n")

# extend() - Merges two lists by adding elements of the second list to the end
a_num = [10, 11, 12]
user_list.extend(a_num)
print(f"Extended list: {user_list}\n")

# insert() - Inserts an element at a specific index (Index, Element)
user_list.insert(12, 13)
print(f"After inserting 13 at index 12: {user_list}\n")

# #remove() = it will rtemove the element which is given as the input in  
user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
user_list.remove(13)
print(f"After removing value 13: {user_list}\n")

#pop() = unlike remove() it takes index as an input and will remove that specific element from the list and also return the list.
user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
popped_val = user_list.pop(-2)
print(f"Popped index -2 (Value: {popped_val}): {user_list}\n")

#count() = count all the available elements in the list.
user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
occurences = user_list.count(2)
print(f"Number of times '2' appears: {occurences}\n")

#sort() = This function will arange the elements in and returns the sorted list.
user_list = [1, 3, 6, 7, 9, 5, 6, 11]
user_list.sort()
print(f"Sorted list: {user_list}\n")

#reverse() =  This function will returns the list in reverse order by giving the elemts fro last to first.
user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
user_list.reverse()
print(f"Reversed list: {user_list}\n")
#copy() = This function will copy the list in to a variable. 
user_list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13]
new_copy = user_list.copy()
print(f"Copied list: {new_copy}\n")

#clear() = It will cleart all the elements in the list and returns an empty list. 
user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
user_list.clear()
print(f"Cleared list: {user_list}\n")



#                                     # python linkes list 
# In python you can pass multiple list into a one single list which is called Linked list. Because of which, it has many benifits in storing, accessing and menuplaitng data.
random_list=[[1,2,3,4,5,6,7,8,9,10],
    [11,12,1,14,15,16,17,18,19,20],
    ['car','bike','scooter','truck','bullock'],
    ['docktor','lawyer','buisness','swipper','it eninier','military'],
    [1,2,3,4,5,6,7,8,9,10,11]]

# Accessing the element at list index 2, inner index 1
print(f"Accessing nested list (index 2,1): {random_list[2][1]}")

# # you can access linked list by indexing or by using loops.


#                                         # List comprehension.
odd_nums = [x for x in range(50) if x%2 !=0]
print(f"Odd numbers using comprehension: {odd_nums}")
