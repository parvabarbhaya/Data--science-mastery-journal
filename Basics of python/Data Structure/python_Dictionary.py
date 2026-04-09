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


                                # Dictionary Comprehension
print("\n--- Dictionary Comprehension ---")
# Dictionary comprehension offers a short syntax for creating a dictionary.

# Example 1: Creating a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
print(f"Dictionary of squares: {squares_dict}")

# Explanation:
# 1. `{...}`: This indicates we are creating a dictionary.
# 2. `num: num**2`: This is the key-value pair. For each item, the item itself (`num`) becomes the key, and its square (`num**2`) becomes the value.
# 3. `for num in numbers`: This is the loop part. It iterates through each `num` in the `numbers` list.

# Example 2: Creating a dictionary with a condition

original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
even_values_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(f"New dictionary with only even values: {even_values_dict}")

# Explanation:
# 1. `original_dict.items()`: This provides the key-value pairs from the original dictionary.
# 2. `for (k, v) in ...`: This loop unpacks each key-value pair into `k` and `v`.
# 3. `if v % 2 == 0`: This is a condition that filters the items, only including the pair if the value `v` is even.


################# Nested dictionary 

# A nested dictionary containing four other dictionaries
students = {
        'student_01': {
            'name': 'Alice',
            'age': 21,
            'major': 'Computer Science'
        },
        'student_02': {
            'name': 'Bob',
            'age': 22,
            'major': 'Physics'
        },
        'student_03': {
            'name': 'Charlie',
            'age': 20,
            'major': 'Mathematics'
        },
        'student_04': {
            'name': 'Diana',
            'age': 23,
            'major': 'Chemistry'
        }
    }

# --- How to work with this nested dictionary ---

# 1. Print the entire nested dictionary
print("--- Complete Nested Dictionary ---")
print(students)
print("\n")

# 2. Accessing information
# To get all details for a specific student (e.g., student_02)
bob_details = students['student_02']
print(f"Details for student_02: {bob_details}")

# To get a specific piece of information (e.g., Charlie's age)
charlie_age = students['student_03']['age']
print(f"Age of student_03 (Charlie): {charlie_age}")
print("\n")

# 3. Modifying a value
# Let's update Diana's major
print(f"Diana's original major: {students['student_04']['major']}")
students['student_04']['major'] = 'Biology'
print(f"Diana's new major: {students['student_04']['major']}")
print("\n")

# 4. Adding a new key-value pair to an inner dictionary
# Let's add a GPA for Alice
print(f"Alice's details before adding GPA: {students['student_01']}")
students['student_01']['gpa'] = 3.8
print(f"Alice's details after adding GPA: {students['student_01']}")
