import random
import string

# Function to generate random characters and numbers
def generate_random():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# Departments list
departments = ["Marketing", "Accounting", "FinOps"]

# User input for department and number of EC2 instances
user_dept = input("Enter your department (Marketing, Accounting, FinOps): ")

# The int function converts a string input into integers
ec2_num = int(input("How many EC2 instances do you want to create? "))

# Check if the user input is in the departments list
if user_dept in ['Marketing', 'Accounting', 'FinOps']:
    
    # Loop through the number of EC2 instances
    for x in range(ec2_num):

        # Combine the user input with the random EC2 instance name
        ec2_name = f"{user_dept}-{generate_random()}"

        # Prints the randomly generated EC2 instance name
        print(f"EC2 Instance {x+1} Name: {ec2_name}")
else:
    print("Error: Invalid department. Please enter 'Marketing', 'Accounting', or 'FinOps'.")