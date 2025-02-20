#import hello_world # If I import a file from this repo, the code inside it will run

# Import random for generating random numbers
import random

# Randint is the function that returns a random integer
print("Display a random number between 1 and 1000:", random.randint(1, 1000))

# Import math for mathematical operations
import math

# Calculating the square root of a number
print("Square root of 25:", math.sqrt(25))

# Import os to interact with the operating system
import os 

# Print the current working directory
print("Current working directory:", os.getcwd())

# Import the matplotlib library to create plots (Command = pip3 install matplotlib)
import matplotlib.pyplot as plt

# Example line plot
x = [1, 2, 3, 4, 5] # X-axis values
y = [1, 4, 9, 16, 25] # Y-axis values

plt.plot(x, y, marker='o') # Plots X and Y with circular markers
plt.title("Simple Line Plot") # This is the tile
plt.xlabel("X Values") # X-axis label
plt.ylabel("Y Values") # Y-axis label
plt.show() # Show the plot