#!/usr/bin/env python3
"""
Gather data from an API
"""
import requests
import sys
from requests.exceptions import HTTPError

url = https://jsonplaceholder.typicode.com
user_id = sys.argv[1]
user = request.get(url + '/users/{}'.format(user_id)).json()
todos = request.get(url + '/todos', params={'userId': user_id}).json()

completed = [task.get('title') for task in todos if task.get('completed') is True]
print('Employee {} is done with tasks({}/{}):'.format(user.get('name'), len(completed), len(todos)))
[print('\t {}'.format(task)) for task in completed]
