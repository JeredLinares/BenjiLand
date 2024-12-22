# Benji's Conway's The Game of Life
# JD Linares
# 2024 12 22

# Created with love for my son 
# to inspire his curiosity

# The hardware is two buttons and a 5x5 LED matrix, controlled by a Raspberry Pi Zero W
# One button iterates starting frames from 1-17, then randomly assignes starting conditions with <50% of the screen filled
# The second button steps though frames based on the starting frame
# This is made in the style of a toddler's wooden block toy

import RPi.GPIO as GPIO     # Depends on Raspberry Pi Zero W's GPIO Pins
#import numpy as np         # Practicing Python, not numpy


# Initalize a global 5x5x17 matrix which will hold the starting conditions
# Account for Python's copy by reference (ie. don't use [[[0]*n]*n]*n])
# ??? Is "starting_conditions" a reserved word?

game_starting_conditions = [[[0 for i in range(5)] for j in range(5)] for k in range(17)]       ## TODO un-hardcode 17
#print(game_starting_conditions)


# Initalize a counter to follow current initall frame
start_counts = 0


# Read starting frames file and set values in starting frames matrix
with open("./input.txt") as starting_frames_data:
    starting_frames_data.readline()                     # Clear description
    number_lines = starting_frames_data.readline()      # Number of starting frames, always of size 5x5
    for frame in range(int(number_lines)):
#        print(starting_frames_data.readline())          # Name of starting frame
        for line_number in range(5):
            line_data = starting_frames_data.readline()             # Line in starting frame
            line_to_set = line_data.strip().split(',')
            line_to_set = [int(item) for item in line_to_set]
            game_starting_conditions[frame][line_number] = line_to_set

#print(game_starting_conditions)
#print(len(game_starting_conditions))


def next_frame():
    """
    # Function to Iterate to next frame
    # Due to 5x5 constraint due to limited GPIO pins on Rasberry pi, act as if continous column 0 to column 4 and row 0 to row 4 (
    # Rule 1:  Any live cell with fewer than 2 live neighbours dies, as if by under population
    # Rule 2:  Any life cell with 2 or 3 live neighbours lives on to the next generation
    # Rule 3:  Any live cell with more than 3 live neighbours dies, as if by under population
    # Rule 4:  Any dead cell with exactly 3 live neighbours becomes a live cell, as if by reproduction
    """





# Loop checking if eather button is pressed




# print("hello world")



