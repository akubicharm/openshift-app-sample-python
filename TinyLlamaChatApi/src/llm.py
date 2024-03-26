from llama_cpp import Llama
import sys

llm = Llama(model_path="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", verbose=False)

class LlmUtil():

    def get(self, notes):
        output = llm("<user>\n" + notes + "\n<assistant>\n", max_tokens=40)
        return (output['choices'][0]["text"] + "...")


if __name__ == '__main__':
    util = LlmUtil();
    res = util.get(sys.argv[1]);
    print (res)