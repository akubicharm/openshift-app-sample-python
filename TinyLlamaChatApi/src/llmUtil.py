from llama_cpp import Llama
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import sys

llm = Llama(model_path="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", verbose=False)

class LlmUtil(Resource):

    def post(self):
        text = request.get_json().get("text") or ""
        system = request.get_json().get("system") or ""
        print(request.get_json())
        output = llm("<user>\n" + text + "\n<assistant>\n" +  "\n<system>\n" + system, max_tokens=40)
        print(output)
        return (output['choices'][0]["text"] + "...")
 


if __name__ == '__main__':
    util = LlmUtil();
    res = util.get(sys.argv[1]);
    print (res)