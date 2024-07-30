#!/usr/bin/python3
"""
python script that, using the requests module, for a given employee id
returns information about his/her todo list progress.

"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    api_url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    api_url_todos = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(api_url_user)
    if user_response.status_code != 200:
        print(f"Error: {user_response.status_code}")
        return

    user_data = user_response.json()
    employee_name = user_data["name"]

    todos_response = requests.get(api_url_todos,
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        print(f"Error: {todos_response.status_code}")
        return

    todos = todos_response.json()

    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)

    # Print the required output
    print(f"Employee {employee_name} is done with \
          tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
