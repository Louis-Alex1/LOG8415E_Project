#!/bin/bash

#Stop the cluster instances
echo "Stopping cluster instances..."
aws ec2 stop-instances --instance-ids i-0b633761237c7d95c > stop.txt
aws ec2 stop-instances --instance-ids i-0919ffd03f5e1e8e7 > stop.txt
aws ec2 stop-instances --instance-ids i-04cb8e3f35c3e24fb > stop.txt
aws ec2 stop-instances --instance-ids i-0924ac68e327f46aa > stop.txt
rm -f stop.txt
echo "Done"