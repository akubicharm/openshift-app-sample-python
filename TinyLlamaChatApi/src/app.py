from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from llmUtil import LlmUtil

app = Flask(__name__)
api = Api(app)
CORS(app)


class HelloWorld(Resource):
    def get(self):
        msg = request.get_json()
        print(msg)        
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(LlmUtil, '/chat')

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
