# Dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y suricata

CMD ["suricata", "-c", "/etc/suricata/suricata.yaml", "-i", "eth0"]