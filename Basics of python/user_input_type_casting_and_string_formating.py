
# This is an practical example of uusing user input, Type casting, and changing types of the variable.

user_input=("Enter some text:")
print("you have enter",user_input)
a='Gautam '
b='Adani'
c= a + '' +b
print(c)
print("Anant\n Ambani")
print("Anant\tAmbani")
print("Anant \ Ambani")

#Format function
name = "Sam"
age = "18"
print("My name  is {} and I am {}  year old ".format(name,age))

# we can also use shorter version of format function which is called as f string.
print(f"My mane is {name} and I am {age} years old.") # this is the most optimam way to use string formation in python.

#Raw string : what raw string does is that it will keep all the quotes, aslash and unique symbol in the form of string useful when working in data calling. 

print(r"r relinace")

#type casting : Type casting is used to convert the type of one variable type to another.

#integer to string
num_int =123
num_str = str(num_int)
print("num_int as string:",num_str)

#string to integer
num_str="456"
num_int=int(num_str)
print("num_str as integer:",num_int)

#float to integer
num_float=3.67
num_int=int(num_float)
print("num_float as integer:",num_int)

#integer to float 
num_int =2990
num_float =float(num_int)
print("num_int as float :",num_int)

# type checking : using the "type()" function we can see the type of each variable.

x=5 
print(type(x))