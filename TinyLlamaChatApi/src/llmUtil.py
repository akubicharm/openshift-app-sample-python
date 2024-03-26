from llama_cpp import Llama
from flask import Flask, request
from flask_restful import Resource, Api
import sys

llm = Llama(model_path="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", verbose=False)

class LlmUtil(Resource):

    def post(self):
        req = request.get_json()
        print(req)
        output = llm("<user>\n" + req['msg'] + "\n<assistant>\n", max_tokens=40)
        return (output['choices'][0]["text"] + "...")


if __name__ == '__main__':
    util = LlmUtil();
    res = util.get(sys.argv[1]);
    print (res)