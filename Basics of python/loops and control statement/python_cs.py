# Welcome to Python Control Statements!
# Think of these as the "Decision Makers" and "Repeaters" of your code.

### 1. IF-ELSE (The Decision Maker)
# Use this when you want the computer to make a choice.

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
elif weather == "rainy":
    print("Take an umbrella!")
else:
    print("Just stay inside.")

# Pro-tip: 'elif' is short for 'else if'. It's like saying "If the first thing isn't true, try this one!"


### 2. FOR LOOPS (The List Follower)
# Use this when you have a collection of things and want to do something to EACH one.

print("\n--- For Loop Example ---")
superheroes = ["Batman", "Superman", "Wonder Woman"]

for hero in superheroes:
    print(f"{hero} is saving the day!")

# You can also use range() to count:
for count in range(1, 4):
    print(f"Counting: {count}")


### 3. WHILE LOOPS (The "Keep Going" Loop)
# Use this when you want to repeat something UNTIL a condition changes.

print("\n--- While Loop Example ---")
battery = 3
while battery > 0:
    print(f"Phone is on... Battery: {battery}%")
    battery -= 1  # We subtract 1 so the loop eventually stops
print("Phone shut down.")


### 4. BREAK and CONTINUE (The Interruptions)
# Sometimes you need to skip a step or stop early.

print("\n--- Break and Continue ---")
for floor in range(1, 6):
    if floor == 2:
        print("Skipping floor 2 (Continue)")
        continue  # Skip the rest of this turn and go to the next floor
    
    if floor == 4:
        print("Elevator broken! (Break)")
        break     # Stop the loop completely
    
    print(f"At floor: {floor}")

"""
QUICK SUMMARY:
- IF: "If this is true, do it once."
- FOR: "Do this for every item in my list."
- WHILE: "Keep doing this until I tell you to stop."
- BREAK: "Stop everything and exit the loop now!"
- CONTINUE: "Skip this specific part and move to the next one."
"""