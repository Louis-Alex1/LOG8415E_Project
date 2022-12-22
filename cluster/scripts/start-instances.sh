#!/bin/bash

#AWS credentials configuration
echo AWS Access Key ID:
read aws_access_key_id

echo AWS Secret Access Key:
read aws_secret_access_key

echo AWS Session Token:
read aws_session_token

aws configure set aws_access_key_id $aws_access_key_id
aws configure set aws_secret_access_key $aws_secret_access_key
aws configure set aws_session_token $aws_session_token
aws configure set region "us-east-1"

#Start the instances
echo "Starting cluster instances..."
aws ec2 start-instances --instance-ids i-04c66e18e95463ab5 > start.txt
aws ec2 start-instances --instance-ids i-0aecb3b6667105909 > start.txt
aws ec2 start-instances --instance-ids i-0c84a77a8aa9b5bc9 > start.txt
aws ec2 start-instances --instance-ids i-0ebaa92895802c983 > start.txt
echo "Done"