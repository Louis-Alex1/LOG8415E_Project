#!/bin/bash
cd "$(dirname "$0")"

#Clean up instances
cd ../terraform
echo Cleaning the instance...
terraform destroy -auto-approve > destroy.txt
rm -f destroy.txt
echo Done!
cd ..