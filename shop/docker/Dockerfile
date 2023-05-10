FROM busybox

# Installer le serveur HTTP BusyBox
RUN addgroup -S http && adduser -S http -G http

# Exposer le port 8080
EXPOSE 8080

# Ajouter une page d'accueil statique
RUN echo "Hello from my E-Shop!" > /home/http/index.html

# Démarrer le serveur HTTP
USER http
CMD ["httpd", "-f", "-p", "8080", "-h", "/home/http"]
