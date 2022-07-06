#!/usr/bin/env python

import yaml

input_file = '1.yml'
dict       = 'versions'

with open(input_file) as f:

    artifacts = yaml.safe_load(f)[dict]

    for key in artifacts:
        if (artifacts[key] != ''):
            print(key + ": " + artifacts[key])
