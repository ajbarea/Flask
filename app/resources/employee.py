from flask import request
from flask_restful import Resource

# Example in-memory database
employees = {
    1: {"name": "John Doe", "age": 30, "position": "Engineer"},
    2: {"name": "Jane Smith", "age": 25, "position": "Designer"},
}


class Employee(Resource):
    def get(self, employee_id):
        """Handle GET request for fetching employee details by ID"""
        employee = employees.get(employee_id)
        if employee:
            return {"status": "success", "data": employee}
        return {"status": "error", "message": "Employee not found"}, 404

    def post(self):
        """Handle POST request for creating a new employee"""
        data = request.json
        if not data or not all(key in data for key in ["name", "age", "position"]):
            return {"status": "error", "message": "Invalid data"}, 400

        employee_id = len(employees) + 1  # Simple auto-increment logic
        employees[employee_id] = {
            "name": data["name"],
            "age": data["age"],
            "position": data["position"],
        }
        return {
            "status": "success",
            "message": "Employee added",
            "id": employee_id,
        }, 201

    def put(self, employee_id):
        """Handle PUT request for updating an employee's details"""
        if employee_id not in employees:
            return {"status": "error", "message": "Employee not found"}, 404

        data = request.json
        if not data or not all(key in data for key in ["name", "age", "position"]):
            return {"status": "error", "message": "Invalid data"}, 400

        employees[employee_id] = {
            "name": data["name"],
            "age": data["age"],
            "position": data["position"],
        }
        return {"status": "success", "message": "Employee updated"}

    def delete(self, employee_id):
        """Handle DELETE request for deleting an employee"""
        if employee_id not in employees:
            return {"status": "error", "message": "Employee not found"}, 404

        del employees[employee_id]
        return {"status": "success", "message": "Employee deleted"}
