#!/bin/bash

#Stop the cluster instances
echo "Stopping cluster instances..."
aws ec2 stop-instances --instance-ids i-02dfa79b79caee93b > stop.txt
aws ec2 stop-instances --instance-ids i-08c6fb6e6efc16128 > stop.txt
aws ec2 stop-instances --instance-ids i-0b3c8ffcb959dfeeb > stop.txt
aws ec2 stop-instances --instance-ids i-05b0ebbbe123a46c0> stop.txt
rm -f stop.txt
echo "Done"