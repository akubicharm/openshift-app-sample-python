from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
app.add_resource(LlmUtil, '/chat')

if __name__ == '__main__':
    app.run(port=8080, debug=True)