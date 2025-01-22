import random
import string

# Function to generate random characters and numbers
def generate_random():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

departments = ["Marketing", "Accounting", "FinOps"]

user_dept = input("Enter your department (Marketing, Accounting, FinOps): ")

ec2_num = int(input("How many EC2 instances do you want to create? "))

# Check if the user input is in the departments list
if user_dept in ['Marketing', 'Accounting', 'FinOps']:
    
    for x in range(ec2_num):

        ec2_name = f"{user_dept}-{generate_random()}"

        print(f"EC2 Instance {x+1} Name: {ec2_name}")
else:
    print("Error: Invalid department. Please enter 'Marketing', 'Accounting', or 'FinOps'.")