#!/bin/bash

#Start the cluster instances
echo "Starting cluster instances..."
aws ec2 start-instances --instance-ids i-0b633761237c7d95c > start.txt
aws ec2 start-instances --instance-ids i-0919ffd03f5e1e8e7 > start.txt
aws ec2 start-instances --instance-ids i-04cb8e3f35c3e24fb > start.txt
aws ec2 start-instances --instance-ids i-0924ac68e327f46aa > start.txt
rm -f start.txt
echo "Done"