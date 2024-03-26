FROM ubi8/python-311
LABEL maintainer="kei.omizo@redhat.com"

WORKDIR /app
USER root
RUN wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

USER 1001
COPY . .

RUN pip install -r requirements.txt


EXPOSE 8080

CMD ["python", "app.py"]