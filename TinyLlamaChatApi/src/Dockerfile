FROM ubi8/python-311
LABEL maintainer="kei.omizo@redhat.com"

RUN pip install ipykernel jupyter
RUN pip install llama-cpp-python
RUN pip install Flask flask_restful

WORKDIR /app
COPY . .

RUN wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf


EXPOSE 8080

CMD ["python", "app.py"]