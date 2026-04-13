"""
Loops are control flow structures that allow code to be executed repeatedly
until a specified condition is met. They enable iteration over sequences
(lists, strings, tuples, etc.) or execution of a block of code multiple times
without writing it repeatedly.

Common types of loops:
- for loops: Iterate over a sequence a fixed number of times
- while loops: Execute as long as a condition remains True
- do-while loops: Execute at least once, then check condition (in some languages)

Key concepts:
- Iteration: Each pass through the loop
- Loop variable: Tracks current position or iteration count
- Condition: Determines when the loop continues or terminates
- Break: Early exit from the loop
- Continue: Skip to the next iteration

Loops are fundamental to programming and enable efficient handling of
repetitive tasks and data processing.
"""# Example of a for loop iterating over a range
print("For loop with range:")
for i in range(5):
    print(f"Iteration {i}")

# Example of a for loop iterating over a list
fruits = ["apple", "banana", "cherry"]
print("\nIterating over a list:")
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Example of a while loop
print("\nWhile loop example:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# Example of break and continue
print("\nLoop with break and continue:")
for n in range(1, 10):
    if n == 3:
        continue  # Skip 3
    if n == 7:
        break     # Stop at 7
    print(n)

# Nested loops
print("\nNested loops:")
for x in range(2):
    for y in range(2):
        print(f"Coordinates: ({x}, {y})")
        
############################ while Loop ###################################
# creating a calculator using a while loop. 
while True:
    try:
        result = eval(input("Enter an expression: "))
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
        break


# creating a password checker using a do while loop 

    while True:
        correct_pass = "Good Morning"
        password = input("Enter the password.")
        if password == correct_pass:
            print(f"the {password} is correct")
            break 
        else:
            print(f"the {password} is incorrect")
            continue