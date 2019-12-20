#!/usr/bin/env python

import requests

#r = requests.get('https://xkcd.com/353/')
#r = requests.get('https://imgs.xkcd.com/comics/python.png')
#payload = {'page': 2, 'count': 25}
payload = {'username': 'amyn', 'password': 'testing'}
#r = requests.get('https://httpbin.org/get', params=payload)
# URL for basic authentication
# https://httpbin.org/basic-auth/corey/testing
#r = requests.post('https://httpbin.org/post', data=payload)
#r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'), timeout=3)
# To see details of the api
# https://httpbin.org/#/Dynamic_data
r = requests.get('https://httpbin.org/delay/6', timeout=3)
#print(dir(r))
#print(help(r))
#print(r.text)

#with open('comic.png', 'wb') as f:
#    f.write(r.content)

print(r.status_code)
# Returns True or False
print(r.ok)

#print(r.headers)

print(r.text)
#print(r.url)

#r_dict = r.json()
#print(r_dict['form'])
