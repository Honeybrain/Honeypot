FROM debian:latest

RUN apt-get update && \
    apt-get install -y fail2ban

COPY fail2ban.conf /etc/fail2ban/
COPY nginx-honeypot.conf /etc/fail2ban/filter.d/

CMD ["fail2ban-client", "-f", "start"]
