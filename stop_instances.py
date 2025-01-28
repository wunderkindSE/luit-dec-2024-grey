import boto3

ec2 = boto3.client('ec2')

response = ec2.stop_instances(InstanceIds=['i-0c1f7b1b4b4b4b4b4']) # Sample EC2 instance ID

print(response)