#!/usr/bin/python3
"""Module to GET data from a json"""
import csv
import json
import requests
import sys


class GetMethod:

    def to_do(employ_id):

        # Setting URLS
        Base_URL = "https://jsonplaceholder.typicode.com"
        Users_url = f"{Base_URL}/users/{employ_id}"
        To_do_URL = f"{Base_URL}/todos"

        # Grabbing employee name and ID
        User = requests.get(Users_url).json()
        username = User.get('username')

        # Setting up to do
        params = {"userId": employ_id}
        todos_total = requests.get(To_do_URL, params=params)
        todos = todos_total.json()

        data = [{
            'task': todo['title'],
            'completed': todo['completed'],
            'username': username
        } for todo in todos]

        # Formatting
        formatted_task = {str(employ_id): data}

        file_name = f'{employ_id}.json'
        with open(file_name, 'w') as file:
            json.dump(formatted_task, file)
        print(f'Data for employee_id {employ_id} written to {file_name}.')


if __name__ == "__main__":

    GetMethod.to_do(int(sys.argv[1]))
