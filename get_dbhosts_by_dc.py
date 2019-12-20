#!/usr/bin/env python

import json
import requests

# Give me all the hosts in FRF dc
url = 'https://heimdall.eng.sfdc.net/pcs-inventory/v1/dbHosts?kingdom=frf'

r = requests.get(url, timeout=10)
if r.ok:
    json_data = r.text
    dic_data = json.loads(json_data)
    host_list = [[h.get(x) for x in ['name', 'isDR']] for h in dic_data['hostList']]
    host_list.sort()
    pri_hosts = []
    dr_hosts = []
    for h_info in host_list:
        if h_info[1] == False:
            pri_hosts.append(h_info[0])
        else:
            dr_hosts.append(h_info[0])

print('=== Primary ===')
for pri_host in pri_hosts:
    print(pri_host)
print('\n')
print('=== DR ===')
for dr_host in dr_hosts:
    print(dr_host)
print('\n')

print('Total Number of hosts: {}'.format(len(dic_data['hostList'])))
print('Total Primary: {}'.format(len(pri_hosts)))
print('Total DR: {}'.format(len(dr_hosts)))
