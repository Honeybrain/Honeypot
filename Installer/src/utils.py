import re
import os
import netifaces
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_valid_cidr(ip):
    try:
        ipaddress.ip_network(ip, strict=False)
        return True
    except ValueError:
        return False

def is_same_subnet(cidr_ips):
    try:
        # Séparation des adresses IP
        ips = [ip.strip() for ip in cidr_ips.split(",")]
        
        # Vérification de chaque adresse IP
        for ip in ips:
            if not ipaddress.ip_address(ip):
                return False
        
        # Création du sous-réseau à partir de la première adresse IP
        network = ipaddress.ip_network(ips[0] + '/24', strict=False)
        
        # Vérification de chaque adresse IP dans le sous-réseau
        for ip in ips[1:]:
            if ipaddress.ip_address(ip) not in network:
                return False
        
        # Toutes les adresses IP sont valides et dans le même sous-réseau
        return True
        
    except ValueError:
        # L'adresse IP n'est pas valide
        return False

def is_valid_ip_list(ip_list):
    # Si c'est une seule IP
    if ',' not in ip_list:
        try:
            ipaddress.ip_address(ip_list)
            return True
        except ValueError:
            return False
    # Si c'est une liste d'IPs
    else:
        ips = ip_list.split(',')
        for ip in ips:
            ip = ip.strip() # Enlever les espaces avant et après
            try:
                ipaddress.ip_address(ip)
            except ValueError:
                return False
    return True

def is_valid_port(port):
    try:
        port = int(port)  # Convertit la chaîne en nombre entier
        return 1 <= port <= 65535
    except ValueError:
        return False

def is_valid_email(email):
    # Expression régulière pour vérifier l'adresse e-mail
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def is_dockerfile_path(path):
    # Vérifie si le chemin existe
    if not os.path.exists(path):
        return False
    
    # Si le mot 'Dockerfile' n'est pas dans le chemin, ajoute le à la fin
    if not path.endswith('Dockerfile'):
        path = os.path.join(path, 'Dockerfile')
    
    # Vérifie si le Dockerfile existe dans le chemin
    return os.path.isfile(path)

def is_valid_interface(interface_name):
    return interface_name in netifaces.interfaces()