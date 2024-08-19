# Objective: The aim of this assignment is to deepen your understanding of Python's range() function.

# Task 1: Your Mood Today:
# Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

import random #imported random package

moods = ["Happy","Sad","Energetic","Calm"] #set list for moods options
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] #set list for days of the week

for day in range(len(days)): # set the following code to run once for each day of the week
    mood = random.choice(moods) # set mood to be = a random choice from the list of moods for each iteration
    print(f"On {days[day]}, you were feeling {mood}.") #printed the statement of mood for each day before moving on to next iteration