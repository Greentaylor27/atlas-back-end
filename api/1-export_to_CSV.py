#!/usr/bin/python3
"""Module to GET data from a json"""
import csv
import json
import requests
import sys


class GetMethod:

    def to_do(employ_id):
        api_url = "https://jsonplaceholder.typicode.com"
        users_url = f"{api_url}/users/{employ_id}"
        todos_url = f"{api_url}/todos"
        user_data = requests.get(users_url).json()
        username = user_data.get('username')

        params = {'userId': employ_id}
        todos_response = requests.get(todos_url, params=params)
        todos = todos_response.json()

        data = [{
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        } for todo in todos]

        formatted_task = {str(employ_id): data}

        file_name = f"{employ_id}.json"
        with open(file_name, 'w') as file:
            json.dump(formatted_task, file)
        print(f"Data for employee_id {employ_id} witten to {file_name}.")


if __name__ == "__main__":

    GetMethod.to_do(int(sys.argv[1]))
