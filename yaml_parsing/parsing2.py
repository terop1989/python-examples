#!/usr/bin/env python

import yaml

with open('2.yml') as f:

    lines = yaml.load_all(f, Loader=yaml.FullLoader)

    for record in lines:
        print(record)

        print("items in record:")
        for item in record:
            print(item)
