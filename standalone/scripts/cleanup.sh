#!/bin/bash
cd "$(dirname "$0")"

#Clean up instances
cd ../terraform
echo Cleaning instances...
terraform destroy -auto-approve > destroy.txt
rm -f destroy.txt
echo Done!
cd ..