# Utiliser une image de base Debian
FROM debian:latest

# Mettre à jour le système
RUN apt-get update

# Installer vsftpd
RUN apt-get install -y vsftpd

# Créer un utilisateur ftp avec un mot de passe
RUN echo "ftpuser:ftppass" | chpasswd

# Créer le dossier de l'utilisateur ftp
RUN mkdir /home/ftpuser/ftp

# Changer les permissions du dossier de l'utilisateur ftp
RUN chown nobody:nogroup /home/ftpuser/ftp

# Activer l'accès en écriture pour l'utilisateur ftp
RUN echo 'write_enable=YES' >> /etc/vsftpd.conf

# Configurer l'utilisateur anonyme pour utiliser le dossier de l'utilisateur ftp
RUN echo 'anon_root=/home/ftpuser/ftp' >> /etc/vsftpd.conf

# Créer le fichier index.html
RUN echo 'Hello, World!' > /home/ftpuser/ftp/index.html

# Exposer le port FTP
EXPOSE 21

# Démarrer vsftpd
CMD /usr/sbin/vsftpd /etc/vsftpd.conf
