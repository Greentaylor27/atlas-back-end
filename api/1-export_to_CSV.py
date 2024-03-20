#!/usr/bin/python3
"""Module to GET data from a json"""
import csv
import json
import requests
import sys


def to_do(employ_id):
    api_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{api_url}/users/{employ_id}"
    todos_url = f"{api_url}/todos"
    user_data = requests.get(users_url).json()
    username = user_data.get('username')

    todos_response = requests.get(todos_url,
                                params={'userId': employ_id}).json()

    file_name = f"{employ_id}.csv"
    with open(file_name, 'w') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_response:
            write.writerow([employ_id, username, 
                            todo['completed'], todo['title']])


if __name__ == "__main__":

    to_do(int(sys.argv[1]))
