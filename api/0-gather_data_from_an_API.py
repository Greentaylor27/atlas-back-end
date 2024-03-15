#!/usr/bin/python3
"""Module to GET data from a json"""
import requests
import sys


class GetMethod:

    def to_do(employ_id):

        employ_id = sys.argv[1]

        # Setting URLS
        Base_URL = "https://jsonplaceholder.typicode.com"
        Users_url = f"{Base_URL}/users/{employ_id}"
        To_do_URL = f"{Base_URL}/todos"

        # Grabbing employee name and ID
        User = requests.get(Users_url)
        Employee_name = User.json().get('name')

        # Setting up to do
        params = {"userId": employ_id}
        todos_total = requests.get(To_do_URL, params=params)
        todos = todos_total.json()
        finished_tasks = [todo for todo in todos if todo['completed']]

        # Formatting
        print(
            f"Employee {Employee_name} is done with tasks"
            f"({len(finished_tasks)}/{len(todos)}):"
        )
        for task in finished_tasks:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    args = int(sys.argv[1])
    GetMethod().to_do()
