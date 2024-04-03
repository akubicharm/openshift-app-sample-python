import ast
from llama_cpp import Llama
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import sys
import datetime

llm = Llama(model_path="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", verbose=False)
# llm = Llama(model_path="ELYZA-japanese-Llama-2-7b-fast-q2_K.gguf", verbose=False)

agentname = "akubi"
current_date = datetime.datetime.now()
formatted_date = current_date.strftime("%m/%d/%Y")
baseprompt = "You are %s, a highly intelligent assistant. Keep your answers brief and accurate. Current date is %s." % (agentname, formatted_date)
context = [{"role": "system", "content": baseprompt}] 


class LlmUtil(Resource):

    def post(self):
        role = request.get_json().get("role") or ""
        prompt = request.get_json().get("text") or ""
        print(role + " " + prompt)
        context.append({"role": role, "content": "Okay, let's get started."})
        context.append({"role": "user", "content": prompt})

        output = llm(
            prompt,
            max_tokens=128,
            temperature=0.3
        )

        print(output)
        return (output['choices'][0])        


if __name__ == '__main__':
    util = LlmUtil();
    res = util.post(sys.argv[1]);
    print (res)