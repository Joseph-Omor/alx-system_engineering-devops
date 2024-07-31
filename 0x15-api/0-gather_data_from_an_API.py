#!/usr/bin/python3
"""
python script that, using the requests module, for a given employee id
returns information about the employee's TODO list progress.

The script fetches user data and TODO list data from a public API and
prints the progress of completed tasks in a specific format.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Parameters:
    employee_id (int): The ID of the employee whose TODO list progress
                        is to be fetched and displayed.
"""


import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress of a given employee.

   The function fetches the employee's name and TODO list from a public API.
   It then calculates the number of completed tasks and the total number of
   tasks, and prints the progress along with the titles of completed tasks.
    """

    """Define the API URLs for fetching user and TODO data"""
    api_url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    api_url_todos = "https://jsonplaceholder.typicode.com/todos"

    """Fetch user data"""
    user_response = requests.get(api_url_user)
    if user_response.status_code != 200:
        """Print an error message if the request was unsuccessful"""
        print(f"Error: {user_response.status_code}")
        return

    """Parse the JSON response to get user data"""
    user_data = user_response.json()
    EMPLOYEE_NAME = user_data["name"]

    """Fetch TODO list data"""
    todos_response = requests.get(api_url_todos,
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        """Print an error message if the request was unsuccessful"""
        print(f"Error: {todos_response.status_code}")
        return

    """Parse the JSON response to get TODO list data"""
    todos = todos_response.json()

    """Calculate the toal number of tasks and the number of completed tasks"""
    TOTAL_NUMBER_OF_TASKS = len(todos)
    completed_tasks = [todo for todo in todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)

    """Print the progress summary"""
    print(f"Employee {EMPLOYEE_NAME} is done with\
          tasks({num_completed_tasks}/{TOTAL_NUMBER_OF_TASKS}):")
    """Print the titles of completed tasks"""
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    """Check if the correct number of command-line arguments is provided"""
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        """Convert the employee ID to an integer"""
        employee_id = int(sys.argv[1])
    except ValueError:
        """Print an error message if the employee ID is not a valid integer"""
        print("Employee ID must be an integer")
        sys.exit(1)

    """Call the function to get and display
    the employee's TODO list progress"""
    get_employee_todo_progress(employee_id)
