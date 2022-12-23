#!/bin/bash

#Start the cluster instances
echo "Starting cluster instances..."
aws ec2 start-instances --instance-ids i-02dfa79b79caee93b > start.txt
aws ec2 start-instances --instance-ids i-08c6fb6e6efc16128 > start.txt
aws ec2 start-instances --instance-ids i-0b3c8ffcb959dfeeb  > start.txt
aws ec2 start-instances --instance-ids i-05b0ebbbe123a46c0 > start.txt
rm -f start.txt
echo "Done"