#!/bin/bash
cd "$(dirname "$0")"

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

#Terraform deploying AWS Infrastructure
cd ../terraform
terraform init
terraform apply -auto-approve
cd ..