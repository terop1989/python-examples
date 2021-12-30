#!/usr/bin/env python

import yaml

with open('1.yml') as f:

    dict = 'versions'
    artifacts = yaml.safe_load(f)['versions']

    for key in artifacts:
        if (artifacts[key] != ''):
            print(key + ": " + artifacts[key])
