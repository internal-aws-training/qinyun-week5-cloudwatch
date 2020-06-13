#!/bin/bash
cd $(dirname $0)/..

FILE_NAME=${1:-template.yml}
echo $FILE_NAME
# Add parameters to cloudformation config file using stackup
stackup qinyun-week5 up -t aws/cloudformation/$FILE_NAME
