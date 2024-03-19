# Utiliser une image de base Ubuntu
FROM ubuntu:latest

# Mettre à jour le système
RUN apt-get update && apt-get upgrade -y

# Installer iproute2
RUN apt-get install -y iproute2

# Installer iputils-ping
RUN apt-get install -y iputils-ping

# Démarrer la machine
CMD ["sleep", "infinity"]