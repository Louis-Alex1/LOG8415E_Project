#!/bin/bash
cd "$(dirname "$0")"

#Clean up the instance
cd ../terraform
echo Cleaning the instance...
terraform destroy -auto-approve > destroy.txt
rm -f destroy.txt
echo Done!
cd ..