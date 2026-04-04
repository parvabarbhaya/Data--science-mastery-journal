# Dictionary practical implementation


person={'name':'parth','age':'40','city':'nz'}

print(f"Accessing value by key 'name': {person['name']}")

print(f"Getting value with .get('age'): {person.get('age')}")

person['city']='Auckland' # Updates the value for the key 'city'
print(f"After updating city: {person}")

person.pop('city') # Removes the 'city' key-value pair
print(f"After popping 'city': {person}")

# The 'del' keyword also deletes a key-value pair from the dictionary.
del person['age']
print(f"After deleting 'age': {person}\n")

# We use the 3 most important things used in dictionaries calles as Keys, values and items.

fruit={'apple':4,'banana':2,'cherry':8}
print(f"All keys in the fruit dictionary: {fruit.keys()}")
print(f"All values in the fruit dictionary: {fruit.values()}")
print(f"All key-value pairs (items) in the fruit dictionary: {fruit.items()}")

fruit.update({'orange':5})
print(f"Dictionary after updating with 'orange': {fruit}\n")

x = {"Good_students":40, 'Bad_Students':20,'students_in_sorts': 10}
#using clear function (will clear all the items form the dict)
y= x.copy()
print(f"Copied dictionary 'y' before clearing: {y}")
y.clear()
print(f"Dictionary 'y' after .clear(): {y}\n")

# using pop function (will pop one item)
x. pop('Good_students')
print(f"Dictionary 'x' after popping 'Good_students': {x}")

# using setdefault function: returns the value of a key. If the key doesn't exist, it inserts the key with a default value.
x.setdefault('students_in_sorts')
print(f"After .setdefault('students_in_sorts'), no change as key exists: {x}")
x.setdefault('new_students', 0)
print(f"After .setdefault('new_students', 0), new key is added: {x}")

# using popitem function (removes the last inserted item in Python 3.7+)
x.popitem()
print(f"Dictionary 'x' after .popitem() (removes last item): {x}\n")


                                      #Advanced Dictionary Techiniques
print("--- Advanced Dictionary Techniques ---")
fruit1 ={'a':1,'b':2}
fruit2={'c':3,'d':4}
fruit1.update(fruit2)
print(f"Merged dictionary (fruit1 updated with fruit2): {fruit1}")

# defaultdict is useful to avoid errors when a key doesn't exist. It provides a default value instead.
from collections import defaultdict
fruit_counts = defaultdict(int) # 'int' provides a default value of 0
fruit_counts['apple'] = 5
print(f"\nAccessing existing key 'apple' in defaultdict: {fruit_counts['apple']}")
print(f"Accessing missing key 'banana' in defaultdict: {fruit_counts['banana']}")
print(f"The defaultdict now contains the new key: {fruit_counts}")

                                # Missing keys using .get()
# The .get() method is another safe way to access keys that might not exist.
fruit={'a':1,'b':2}
print(f"\nUsing .get() for a missing key 'c' with a default value of 0: {fruit.get('c', 0)}")
print(f"The original dictionary is unchanged: {fruit}")


#orderdict()
# OrderedDict remembers the order that keys were first inserted.
# Note: Since Python 3.7, standard dictionaries also preserve insertion order.
from collections import OrderedDict
fruit=OrderedDict()
fruit['a']=1
fruit['b']=2
fruit['c']=3
print(f"\nKeys from OrderedDict (insertion order is preserved): {fruit.keys()}")



                                #storing a list of items in a dictionary.

names = [['car','bike','scooter','truck','bullock'],
    ['docktor','lawyer','buisness','swipper','it eninier','military']]

new_dict = dict()
new_dict['vehical'] = names[0]
new_dict['occupation'] = names[1]
print(f"\nDictionary created from a list of lists: {new_dict}")
print(f"Accessing the list of vehicles: {new_dict['vehical']}")
