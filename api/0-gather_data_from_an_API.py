import requests
import sys
"""Module to GET data from a json"""

class GetMethod:

    def to_do(employ_id):

        # Setting URLS
        Base_URL = "https://jsonplaceholder.typicode.com"
        Users_URL =  requests.get(Base_URL + "/users")
        To_do_URL = requests.get(Base_URL + "/todo")

        # Setting up JSONS
        User_json = Users_URL.json()
        To_Do_json = To_do_URL.json()

        #Pulling name and ID from User_json
        for item in User_json:
            name = item['name']
            id = item['id']

        # Testing
        if User_json[id] == To_Do_json[id]:
            print("Well done")

    # def employee_name(ident):
        # Base_URL = "https://jsonplaceholder.typicode.com/users/"

if __name__ == "__main__":
    args = sys.argv
    GetMethod().to_do()
