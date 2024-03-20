FROM alpine:latest

RUN apk update && apk upgrade

RUN apk add python3

COPY generator.py .

CMD ["sleep", "infinity"]