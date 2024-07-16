#!/usr/bin/python3
""" Export to json """

import json
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'
user_id = sys.argv[1]
user = requests.get(url + 'users/{}'.format(user_id)).json()
username = user.get("username")
todos = requests.get(url + 'todos', params = {'userId': user_id}).json()

with open("{}.json".format(user_id), "w") as jsonfile:
    for task in todos:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }]}, jsonfile)  # json.dump writes to a file
