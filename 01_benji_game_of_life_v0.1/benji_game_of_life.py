# Benji's Conway's The Game of Life
# JD Linares
# Created: 2024 12 22
# Last update: 2024 12 27

# Created with love for my son 
# May it inspire his curiosity love for knowledge

# The hardware is two buttons and a 5x5 LED matrix, controlled by a Raspberry Pi Zero W
# One button iterates starting frames from 1-17, then randomly assignes starting conditions with <50% of the screen filled
# The second button steps though frames based on the starting frame
# This is made in the style of a toddler's wooden block toy

from gpiozero import LED, Button        # Depends on Raspberry Pi Zero W's GPIO Pins
#import numpy as np                     # Practicing Python, not numpy
from signal import pause                #
from time import sleep                  #

butt1 = Button(25)                      # Sets screen to next inital frame
butt2 = Button(26)                      # Increments frame
led_set = [ 0 for x in range(25)]

# Initalize the 5x5 matrix of LEDs
for led_num in range(25):
	led_set[led_num] = LED(led_num)
	led_set[led_num].off()


# Debug 5x5 matrix
# Debug - All off / on
def debug_func1():
	for led_num in range(25):
		led_set[led_num].off()
def debug_func2():
	for led_num in range(25):
		led_set[led_num].on()
'''
debug_func1()
sleep(5)
debug_func2()
sleep(5)
debug_func1()
sleep(5)
'''

# Initalize a global 5x5x17 matrix which will hold the starting conditions
# Account for Python's copy by reference (ie. don't use [[[0]*n]*n]*n], instead use [ 0 for x in range(25) ]

game_starting_conditions = [[[0 for i in range(5)] for j in range(5)] for k in range(17)]       ## TODO evenutally un-hardcode 17
#print(game_starting_conditions)

# Initalize a counter to follow current initall frame
start_counts = 0


# Read starting frames file and set values in starting frames matrix
with open("./input.txt") as starting_frames_data:
    starting_frames_data.readline()                     # Clear description
#    print(starting_frames_data)
    number_lines = starting_frames_data.readline()      # Number of starting frames, always of size 5x5
#    print(number_lines)
    for frame in range(int(number_lines)):
        frame_name = starting_frames_data.readline()
#        print(frame_name)          # Name of starting frame
        for line_number in range(5):
            line_data = starting_frames_data.readline()             # Line in starting frame
            line_to_set = line_data.strip().split(',')
            line_to_set = [int(item) for item in line_to_set]
            game_starting_conditions[frame][line_number] = line_to_set
#print(game_starting_conditions)

# Set starting frame
current_frame = game_starting_conditions[0]

def next_frame(pass_current_frame):
    """
    # Function to Iterate to next frame
    # Due to 5x5 constraint due to limited GPIO pins on Rasberry pi, act as if continous column 0 to column 4 and row 0 to row 4 (
    # Rule 1:  Any live cell with fewer than 2 live neighbours dies, as if by under population
    # Rule 2:  Any live cell with 2 or 3 live neighbours lives on to the next generation
    # Rule 3:  Any live cell with more than 3 live neighbours dies, as if by over population
    # Rule 4:  Any dead cell with exactly 3 live neighbours becomes a live cell, as if by reproduction
    """
    
    # Define a 5x5 array to return as the next frame
    next_frame = [[0 for x in range(5)] for y in range(5)]

    #iterate though next_frame calculating births/deaths/stays
    for row in range(5):
        for element in range(5):
            # Count number of alive cells around the new cell from the current frame and store in next_frame
            number_alive_cells = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if( x!=0 or y!=0 ):    #this has to be complicated because python doesn't let you leave empty if statements
                        number_alive_cells += pass_current_frame[ (row + x) % 5 ][ (element + y) % 5 ]
            if number_alive_cells < 2:
                next_frame[row][element] = 0
            elif number_alive_cells > 3:
                next_frame[row][element] = 0
            elif number_alive_cells == 2:
                next_frame[row][element] = current_frame[row][element]
            elif number_alive_cells == 3: 
                next_frame[row][element] = 1
    return next_frame

# For Debugging: iterate though 10 steps of each starting case to confirm expected output
def debug_func3():
    print("Debugger output")
    for starter in range(17):
        current_frame = game_starting_conditions[starter]
        print()
        print()
        print("Restart " + str(starter))
        [print(output_row) for output_row in current_frame]
        print()
        for step in range(10):
            current_frame = next_frame()
            [print(output_row) for output_row in current_frame]
            print()

# Function to set LEDs based on a 5x5 matrix
def set_LED_matrix(the_inital_frame):    # input must be 5x5
    for i in range(5):
        for j in range(5):
            if the_inital_frame[i][j] == 1:
                led_set[i+5*j].on()               # LEDs are setup sequentially from 0-24
            else:
                led_set[i+5*j].off()


# Setup Button 1 Funtion: Go to next inital frame 
def set_next_inital_frame():
    print("button 1 function")
    global start_counts 
    start_counts =  (start_counts + 1)%16       ## TODO change this to generate random start after 17
    global current_frame
    current_frame = game_starting_conditions[start_counts]
    set_LED_matrix(current_frame)

# Setup Button 2 Function: Step to next frame
def iterate_LED_frame():
    print("button 2 function")
    global current_frame
    next_frame_to_show = next_frame(current_frame)
    current_frame = next_frame_to_show
    set_LED_matrix(current_frame)

# Start the game at the first inital frame
set_LED_matrix(current_frame)

# Setup Buttons
butt1.when_pressed = set_next_inital_frame
butt2.when_pressed = iterate_LED_frame

pause()

