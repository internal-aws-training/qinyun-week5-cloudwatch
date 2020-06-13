#!/bin/bash
cd $(dirname $0)/..

# Add parameters to cloudformation config file using stackup
stackup qinyun-week5 up -t aws/cloudformation/template.yml