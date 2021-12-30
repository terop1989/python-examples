#!/usr/bin/env python

import time, datetime
today = datetime.datetime.now()

path_to_log_file = '/var/log/nginx/access.log'
log_file = open(path_to_log_file, 'r')

ip_list = []

for line in log_file:
  dt = line.split()[3].lstrip('[')
  dt_obj = datetime.datetime.strptime(dt, '%d/%b/%Y:%H:%M:%S')
  delta = (today - dt_obj).total_seconds()

  if (delta <= 7200) :
    ip = line.split()[0]
    if (ip not in ip_list) :
      ip_list.append(ip)
      print (ip)

log_file.close
