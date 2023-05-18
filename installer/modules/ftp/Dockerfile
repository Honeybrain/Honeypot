# Utiliser une image de base Debian
FROM debian:latest

# Mettre à jour le système
RUN apt-get update

# Installer vsftpd
RUN apt-get install -y vsftpd

# Créer un utilisateur ftp
RUN useradd -m ftpuser

# Définir le mot de passe pour l'utilisateur ftp
RUN echo "ftpuser:ftppass" | chpasswd

# Créer le dossier de l'utilisateur ftp
RUN mkdir /home/ftpuser/ftp

# Changer les permissions du dossier de l'utilisateur ftp
RUN chown ftpuser:ftpuser /home/ftpuser/ftp

# Activer l'accès en écriture pour l'utilisateur ftp
RUN echo 'write_enable=YES' >> /etc/vsftpd.conf

# Configurer l'utilisateur anonyme pour utiliser le dossier de l'utilisateur ftp
RUN echo 'local_root=/home/ftpuser/ftp' >> /etc/vsftpd.conf
RUN echo 'user_sub_token=$USER' >> /etc/vsftpd.conf
RUN echo 'local_umask=022' >> /etc/vsftpd.conf
RUN echo 'chroot_local_user=YES' >> /etc/vsftpd.conf

# Activer la connexion anonyme
RUN echo 'anonymous_enable=YES' >> /etc/vsftpd.conf
RUN echo 'no_anon_password=YES' >> /etc/vsftpd.conf
RUN echo 'anon_root=/home/ftpuser/ftp' >> /etc/vsftpd.conf
RUN echo 'anon_umask=022' >> /etc/vsftpd.conf

# Créer le fichier index.html
RUN echo 'Hello, World!' > /home/ftpuser/ftp/index.html

# Créer le répertoire 'empty' pour secure_chroot_dir
RUN mkdir -p /var/run/vsftpd/empty && \
    chmod 555 /var/run/vsftpd/empty

# Utiliser le répertoire 'empty' pour secure_chroot_dir
RUN echo 'secure_chroot_dir=/var/run/vsftpd/empty' >> /etc/vsftpd.conf

# Exposer le port FTP
EXPOSE 21

# Démarrer vsftpd
CMD /usr/sbin/vsftpd /etc/vsftpd.conf
