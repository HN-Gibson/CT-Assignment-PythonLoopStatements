# Objective: The aim of this assignment is to practice using nested loops in Python.

# Task 1: Your Mood Tracker:
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.

import random #imported random package

moods = ["Happy","Sad","Energetic","Calm"] #set list for moods options
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] #set list for days of the week
times = ["morning", "afternoon", "evening"] #set list for times of day

for day in days: # set the following code to run once for each day of the week
    for time in times: # Simply added a nested for statement to the_range_riddle.py to run the same basic loop for the time of each day
        mood = random.choice(moods) # set mood to be = a random choice from the list of moods for each iteration
        print(f"On {day} {time}, you we feeling {mood}.") #printed the statement of mood for each time of day before moving on to next iteration