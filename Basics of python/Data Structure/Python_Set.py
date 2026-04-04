# define set : It is an unordered collection of multiple items who has differnet data types.

# in python the set are unindexed and a collection of an unique items stored in it. 

# A set can store a None values.

# A set screates a hah table internally when it is being created.
 
# A set is being denoted using the {}.

s =  {1,2,3,4,5,6,7}
print(f"Basic Set: {s}")

# you can aslo use a set function to create a set.

new_set = set('India')
print(f"Set created from string 'India': {new_set}")

# adding list to the set.
team_list = ['India', 'WestIndies','Australiya']
cricket_set = set(team_list)
print(f"Set created from list: {cricket_set}")
# converting tupel in to a set
team_tup = ('India', 'WestIndies','Australiya')
converted_tuple = set(team_tup)
print(f"Set created from tuple: {converted_tuple}")
# converting tupel in to a set
team_dict = {'India':1, 'WestIndies':2,'Australiya':3}
converted_dict = set(team_dict)
print(f"Set created from dictionary (keys only): {converted_dict}")

# Note: in set you cannot use indexing to locate and fetch the data. 
############################################################

# Adding Elements to the set:
set_1 = set(team_list)
set_1.add('Brazil')
print(f"After adding 'Brazil': {set_1}")

# update elements in the set
set_2 = set(team_list)
set_2.update(['china', 'south koriya', 'USA'])
print(f"After updating with multiple items: {set_2}")
# Removing elements from the set
set_3 = set(team_list)
set_3.remove('India')
print(f"After removing 'India': {set_3}")
# Discarding an element from the set.
# Means: Removing an element from the set, but ignoring it if it dosen't exist.

set_3.discard('Australiya')
print(f"After discarding 'Australiya': {set_3}")

# using pop function in set. 
set_3.pop()
print(f"After popping a random element: {set_3}")

# using clear function in the set. 
set_4 = set_1.copy()
set_4.clear()

# set opeartions :

# In set thaere are different operations which are also being used for many purpose eg: Unioun, Diffenrence, Intersection, Systematic_differance.

# create two different sets 
set_5 = {1,2,3,4,5} 
set_6 = (4,5,6,7,8,9,10)
print(f"\nTuple set_6 to be used in operations: {set_6}")

# Set unioun is 
set_7 = set_5.union(set_6)
print(f"Union of set_5 and set_6: {set_7}")
# it will marge all the numbers in to one single set

# set intersection.
set_8 = set_5.intersection(set_6) 
print(f"Intersection of set_5 and set_6: {set_8}")

# Differnece of two sets.
set_9 = set_5.difference(set_6)
print(f"Difference (set_5 - set_6): {set_9}")

# Systematic differance.

set_10 = set_5.symmetric_difference(set_6)
print(f"Symmetric Difference of set_5 and set_6: {set_10}")

########################################
# How would you access an single element in the set 

# It can be done through using forloop.

print("\nIterating through set_1:")
for i in set_1:
    print(f"Element: {i}")


############################################################################################################################




################### Frozen Set ###############################

# In python just like set there are Frozen Sets : It is a bult- in data type that is similiar to a set but it is immutable. Means if we modify it's elements we cannot change any elements in it like adding, updating and removing elements it does not duplicate any values. 

# Eg of frozenset is

FS = frozenset([1000,20000,20000,44000,50000])
print(f"\nFrozen Set (duplicates removed, immutable): {FS}") 