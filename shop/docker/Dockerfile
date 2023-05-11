FROM busybox

# Installer le serveur HTTP BusyBox
RUN addgroup -S http && adduser -S http -G http

# Exposer le port 8080
EXPOSE 8080

# Copier le fichier index.html dans le conteneur
COPY ./index.html /home/http/index.html

# Démarrer le serveur HTTP
USER http
CMD ["httpd", "-f", "-p", "8080", "-h", "/home/http"]
