from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)  # create Flask instance
api = Api(app)  # API router


class HelloWorld(Resource):
    def get(self):  # Handles 'get' request
        return {"message": "Hello, World!"}


api.add_resource(HelloWorld, "/hi")  # API 'endpoint'

if __name__ == "__main__":
    app.run(port=8000, debug=True)
