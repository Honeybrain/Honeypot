FROM alpine:latest

RUN apk update && apk add --no-cache python3 py3-pip

RUN pip install jinja2 --break-system-packages

COPY generator.py /generator.py

CMD ["sleep", "infinity"]
