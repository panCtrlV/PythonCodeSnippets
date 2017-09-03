# -*- coding: utf-8 -*-
# @Author: Pan Chao
# @Date:   2017-09-03 17:17:33
# @Last Modified by:   Pan Chao
# @Last Modified time: 2017-09-03 17:25:10

'''
Reference:
    - http://docs.python-requests.org/en/master/user/quickstart/
'''

import requests

# Make a Request
r = requests.get('https://api.github.com/events')
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

# Passing Parameters In URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# Get Response Content
r = requests.get('https://api.github.com/events')
r.text
r.encoding
r.encoding = 'ISO-8859-1'

# Parse JSON Response Content
r = requests.get('https://api.github.com/events')
r.json()

# Custom HTTP headers
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

# Access and Send Cookies
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text

# Timeouts
requests.get('http://github.com', timeout=0.001)