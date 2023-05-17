FROM busybox

# Installer le serveur HTTP BusyBox
RUN addgroup -S http && adduser -S http -G http

# Exposer le port 8081
EXPOSE 8081

# Ajouter une page d'accueil statique
RUN echo "Hello from my Honeypot!" > /home/http/index.html

# Démarrer le serveur HTTP en tant qu'utilisateur root
USER root
CMD ["httpd", "-f", "-p", "8081", "-h", "/home/http"]
