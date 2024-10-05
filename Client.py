# client.py

import requests
import json

# Base URL of the Flask API
BASE_URL = "http://localhost:5000/employee"


# Function to fetch employee data by ID
def fetch_employee(employee_id):
    try:
        url = f"{BASE_URL}/{employee_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


# Function to create a new employee
def create_employee(name, age, position):
    try:
        data = {"name": name, "age": age, "position": position}
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            BASE_URL, data=json.dumps(data), headers=headers, timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


# Function to update an existing employee by ID
def update_employee(employee_id, name, age, position):
    try:
        url = f"{BASE_URL}/{employee_id}"
        data = {"name": name, "age": age, "position": position}
        headers = {"Content-Type": "application/json"}
        response = requests.put(url, data=json.dumps(data), headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


# Function to delete an employee by ID
def delete_employee(employee_id):
    try:
        url = f"{BASE_URL}/{employee_id}"
        response = requests.delete(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Fetch employee data
    employee_data = fetch_employee(1)
    if employee_data:
        print("Fetched Employee:", employee_data)
    else:
        print("Failed to fetch employee data.")

    # Create a new employee
    new_employee = create_employee("Alice Johnson", 29, "Developer")
    if new_employee:
        print("New Employee Created:", new_employee)
    else:
        print("Failed to create employee.")

    # Update an existing employee
    updated_employee = update_employee(1, "John Doe", 35, "Senior Engineer")
    if updated_employee:
        print("Employee Updated:", updated_employee)
    else:
        print("Failed to update employee.")

    # Delete an employee
    delete_response = delete_employee(2)
    if delete_response:
        print("Employee Deleted:", delete_response)
    else:
        print("Failed to delete employee.")
