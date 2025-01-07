# Import the Boto3 library to interact with AWS services
import boto3

#Creates and returns an EC2 client using Boto3
def get_ec2_client() -> boto3.client:

    return boto3.client('ec2')

#Creates and returns an S3 client using Boto3
def get_s3_client() -> boto3.client:

    return boto3.client('s3')

#Describes EC2 instances and returns a list of instances
#def describe_instances(client: boto3.client) -> list: