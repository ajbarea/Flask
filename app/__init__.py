from flask import Flask
from flask_restful import Api
from .resources.employee import Employee


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Register resource endpoints
    api.add_resource(Employee, "/employee/<int:employee_id>", "/employee")

    return app
