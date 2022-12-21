#!/bin/bash
cd "$(dirname "$0")"

#Clean up instances
cd ../terraform
echo Cleaning instances...
rm -f destroy.txt
terraform destroy -auto-approve > destroy.txt
echo Done!
cd ..