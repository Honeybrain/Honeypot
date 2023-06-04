
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import ipaddress
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
from generator import generate
import json
import os
import sys
import threading
import webbrowser
import re
import netifaces

OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH_PAGE_1 = OUTPUT_PATH / Path(r"assets/frame4")
def relative_to_assets_page_1(path: str) -> Path:
    return ASSETS_PATH_PAGE_1 / Path(path)

ASSETS_PATH_PAGE_2 = OUTPUT_PATH / Path(r"assets/frame3")
def relative_to_assets_page_2(path: str) -> Path:
    return ASSETS_PATH_PAGE_2 / Path(path)

ASSETS_PATH_PAGE_3 = OUTPUT_PATH / Path(r"assets/frame2")
def relative_to_assets_page_3(path: str) -> Path:
    return ASSETS_PATH_PAGE_3 / Path(path)

ASSETS_PATH_PAGE_4 = OUTPUT_PATH / Path(r"assets/frame0")
def relative_to_assets_page_4(path: str) -> Path:
    return ASSETS_PATH_PAGE_4 / Path(path)

ASSETS_PATH_PAGE_5 = OUTPUT_PATH / Path(r"assets/frame5")
def relative_to_assets_page_5(path: str) -> Path:
    return ASSETS_PATH_PAGE_5 / Path(path)

ASSETS_PATH_PAGE_6 = OUTPUT_PATH / Path(r"assets/frame6")
def relative_to_assets_page_6(path: str) -> Path:
    return ASSETS_PATH_PAGE_6 / Path(path)

ASSETS_PATH_PAGE_7 = OUTPUT_PATH / Path(r"assets/frame7")
def relative_to_assets_page_7(path: str) -> Path:
    return ASSETS_PATH_PAGE_7 / Path(path)

ASSETS_PATH_PAGE_8 = OUTPUT_PATH / Path(r"assets/frame8")
def relative_to_assets_page_8(path: str) -> Path:
    return ASSETS_PATH_PAGE_8 / Path(path)

window = Tk()

window.geometry("862x519")
window.configure(bg = "#003061")

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

def page1():
    canvas = Canvas(
        window,
        bg = "#003061",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        430.9999999999999,
        0.0,
        861.9999999999999,
        519.0,
        fill="#FCFCFC",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets_page_1("image_1.png"))
    image_1 = canvas.create_image(
        645.9999999999999,
        237.0,
        image=image_image_1
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_page_1("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page2(),
        relief="flat"
    )
    button_2.place(
        x=556.9999999999999,
        y=401.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        39.999999999999886,
        127.0,
        anchor="nw",
        text="Bienvenue sur Honeybrain",
        fill="#FCFCFC",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_rectangle(
        39.999999999999886,
        160.0,
        99.99999999999989,
        165.0,
        fill="#FCFCFC",
        outline="")

    canvas.create_text(
        39.999999999999886,
        186.0,
        anchor="nw",
        text="Sécurisez vos projets en déployant",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        39.999999999999886,
        214.0,
        anchor="nw",
        text="notre solution tout-en-un !",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        39.999999999999886,
        214.0,
        anchor="nw",
        text="notre solution tout-en-un !",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        39.999999999999886,
        242.0,
        anchor="nw",
        text="Détectez les attaques grâce",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        39.999999999999886,
        270.0,
        anchor="nw",
        text="à notre honeypot facile à installer et",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        39.999999999999886,
        298.0,
        anchor="nw",
        text="et protégez votre site internet.",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )
    window.mainloop()


def page2():
    global page2_entry_1
    global page2_entry_2
    canvas = Canvas(
        window,
        bg = "#003061",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets_page_2("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page3(),
        relief="flat"
    )
    button_1.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        40.0,
        43.00000000000001,
        anchor="nw",
        text="Honeybrain setup :",
        fill="#FCFCFC",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_rectangle(
        40.0,
        77.0,
        100.0,
        82.0,
        fill="#FCFCFC",
        outline="")

    canvas.create_text(
        40.0,
        388.0,
        anchor="nw",
        text="Configurez et déployez votre",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        417.0,
        anchor="nw",
        text="Honeypot depuis cet installateur sur",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        446.0,
        anchor="nw",
        text="votre site en production. ",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        98.0,
        anchor="nw",
        text="Honeybrain vise à détecter et attirer les ",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        127.0,
        anchor="nw",
        text="attaquants potentiels en simulant des",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        156.0,
        anchor="nw",
        text="services vulnérables, et grâce à son ",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        185.0,
        anchor="nw",
        text="dashboard d'administration et ses",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        214.0,
        anchor="nw",
        text="blocages d'IP automatisés, il permet ",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        243.0,
        anchor="nw",
        text="de surveiller les activités des attaquants",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        272.0,
        anchor="nw",
        text="et de bloquer les adresses IP",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        301.0,
        anchor="nw",
        text="suspectes pour renforcer la sécurité de",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        330.0,
        anchor="nw",
        text="de votre système.",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets_page_2("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        646.5,
        311.5,
        image=entry_image_1
    )
    page2_entry_1 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page2_entry_1.insert('1', '192.168.1.0/24')
    page2_entry_1.place(
        x=486.0,
        y=281.0,
        width=321.0,
        height=59.0
    )

    canvas.create_text(
        475.0,
        253.0,
        anchor="nw",
        text="Sous réseau de votre réseau Honeypot :",
        fill="#FFFFFF",
        font=("Roboto Bold", 16 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets_page_2("entry_1.png"))
    entry_bg_2 = canvas.create_image(
        646.5,
        189.5,
        image=entry_image_2
    )
    page2_entry_2 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page2_entry_2.insert('1', 'eth0')
    page2_entry_2.place(
        x=486.0,
        y=159.0,
        width=321.0,
        height=59.0
    )

    canvas.create_text(
        475.0,
        133.0,
        anchor="nw",
        text="Interface réseau à espionner :",
        fill="#FFFFFF",
        font=("Roboto Bold", 16 * -1)
    )

    window.mainloop()

def page3():
    global page3_entry_1
    global page3_entry_2

    def page3_button_2_clicked():
        global nofakemachine
        nofakemachine = True
        page4(nofakemachine)

    def page3_button_1_clicked():
        global nofakemachine
        nofakemachine = False
        page4(nofakemachine)

    if not is_valid_interface(page2_entry_2.get()):
        messagebox.showerror("Erreur.", "Cette interface réseau n'existe pas. Tapez ifconfig pour trouver le nom de votre interface réseau (du paquet npm net-tools).")
        page2()

    if not is_valid_cidr(page2_entry_1.get()):
        messagebox.showerror("Erreur.", "Ceci n'est pas une adresse IP.")
        page2()

    canvas = Canvas(
        window,
        bg = "#003061",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        431.0,
        0.0,
        862.0,
        519.0,
        fill="#FCFCFC",
        outline="")

    canvas.create_text(
        474.0,
        197.0,
        anchor="nw",
        text="(example: 192.168.1.16, 192.168.1.32) ",
        fill="#505485",
        font=("Roboto Bold", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets_page_3("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page3_button_2_clicked(),
        relief="flat"
    )
    button_1.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_page_3("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page3_button_1_clicked(),
        relief="flat"
    )
    button_2.place(
        x=557.0,
        y=331.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        40.0,
        127.0,
        anchor="nw",
        text="Module fake machines",
        fill="#FCFCFC",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_text(
        474.0,
        63.00000000000001,
        anchor="nw",
        text="Nombre de machines:",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        475.0,
        178.0,
        anchor="nw",
        text="IP spécifiques:",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_rectangle(
        40.0,
        160.0,
        100.0,
        165.0,
        fill="#FCFCFC",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets_page_3("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        646.5,
        126.5,
        image=entry_image_1
    )
    page3_entry_1 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page3_entry_1.place(
        x=486.0,
        y=96.0,
        width=321.0,
        height=59.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets_page_3("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        646.5,
        271.5,
        image=entry_image_2
    )
    page3_entry_2 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page3_entry_2.place(
        x=486.0,
        y=241.0,
        width=321.0,
        height=59.0
    )

    canvas.create_text(
        40.0,
        186.0,
        anchor="nw",
        text="Générez de fausses machines à la",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        214.0,
        anchor="nw",
        text="volée ces machines seront visibles",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        242.0,
        anchor="nw",
        text="sur le réseau du honeypot pour",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        270.0,
        anchor="nw",
        text="simuler un environnement dans",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        298.0,
        anchor="nw",
        text="une entreprise.",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    window.mainloop()

def page4(nofakemachine):
    global page4_entry_1
    global page4_entry_2

    def page4_button_2_clicked():
        global noftp
        noftp = True
        page5(noftp)

    def page4_button_1_clicked():
        global noftp
        noftp = False
        page5(noftp)

    if nofakemachine is not False:
        if not is_valid_ip_list(page3_entry_2.get()):
            messagebox.showerror("Erreur.", "Le format de la liste est invalide.")
            page3()
        
        if not is_same_subnet(page3_entry_2.get()):
            messagebox.showerror("Erreur.", "Au moins une IP n'est pas dans le sous réseau: " + page2_entry_1.get())
            page3()

    canvas = Canvas(
        window,
        bg = "#003061",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        431.0,
        7.105427357601002e-15,
        866.0,
        519.0,
        fill="#FCFCFC",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets_page_3("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page4_button_2_clicked(),
        relief="flat"
    )
    button_1.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        40.0,
        127.0,
        anchor="nw",
        text="Module serveur FTP",
        fill="#FCFCFC",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_text(
        474.0,
        90.0,
        anchor="nw",
        text="Adresse IP du serveur:",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        474.0,
        207.0,
        anchor="nw",
        text="Port du serveur:",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_rectangle(
        40.0,
        160.0,
        100.0,
        165.0,
        fill="#FCFCFC",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets_page_3("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        646.5,
        153.5,
        image=entry_image_1
    )
    page4_entry_1 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page4_entry_1.place(
        x=486.0,
        y=123.0,
        width=321.0,
        height=59.0
    )

    canvas.create_text(
        40.0,
        186.0,
        anchor="nw",
        text="Générez un serveur FTP factice",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        214.0,
        anchor="nw",
        text="accessible sur la même adresse IP que",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        242.0,
        anchor="nw",
        text="votre site en production, tout en le",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        270.0,
        anchor="nw",
        text="gardant sur un réseau virtuel séparé",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        299.0,
        anchor="nw",
        text="garantissant une isolation de",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        327.0,
        anchor="nw",
        text="l’attaquant.",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_page_3("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page4_button_1_clicked(),
        relief="flat"
    )
    button_2.place(
        x=557.0,
        y=331.0,
        width=180.0,
        height=55.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets_page_3("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        646.5,
        271.5,
        image=entry_image_2
    )
    page4_entry_2 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page4_entry_2.insert('1', '21')
    page4_entry_2.place(
        x=486.0,
        y=241.0,
        width=321.0,
        height=59.0
    )
    window.mainloop()

def page5(noftp):
    global page5_entry_1
    global page5_entry_2
    if noftp is not False:
        if not is_valid_ip_list(page4_entry_1.get()):
            messagebox.showerror("Erreur.", "Adresse IP invalide.")
            page4()

        if not is_valid_port(page4_entry_2.get()):
            messagebox.showerror("Erreur.", "Port invalide.")
            page4()

    canvas = Canvas(
        window,
        bg = "#003061",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets_page_5("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page6(),
        relief="flat"
    )
    button_1.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        258.0,
        61.00000000000001,
        anchor="nw",
        text="on y est presque ...",
        fill="#FCFCFC",
        font=("Roboto Bold", 40 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets_page_5("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        430.5,
        329.5,
        image=entry_image_1
    )
    page5_entry_1 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page5_entry_1.place(
        x=278.0,
        y=299.0,
        width=305.0,
        height=59.0
    )

    canvas.create_text(
        266.0,
        275.0,
        anchor="nw",
        text="Mot de passe :",
        fill="#FFFFFF",
        font=("Roboto Bold", 16 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets_page_5("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        430.5,
        231.5,
        image=entry_image_2
    )
    page5_entry_2 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page5_entry_2.place(
        x=278.0,
        y=201.0,
        width=305.0,
        height=59.0
    )

    canvas.create_text(
        266.0,
        177.0,
        anchor="nw",
        text="E-mail :",
        fill="#FFFFFF",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        149.0,
        113.0,
        anchor="nw",
        text="Créez votre compte administrateur pour accéder au dashboard",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        274.0,
        141.0,
        anchor="nw",
        text="d’administration de votre honeypot.",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )
    window.mainloop()

def page6():
    global page6_entry_1
    if not is_valid_email(page5_entry_2.get()):
        messagebox.showerror("Erreur.", "E-mail invalide.")
        page5()

    canvas = Canvas(
        window,
        bg = "#003061",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets_page_8("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page7(),
        relief="flat"
    )
    button_1.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        252.0,
        61.00000000000001,
        anchor="nw",
        text="une dernière étape !",
        fill="#FCFCFC",
        font=("Roboto Bold", 40 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets_page_8("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        431.0,
        274.5,
        image=entry_image_1
    )
    page6_entry_1 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page6_entry_1.place(
        x=178.0,
        y=244.0,
        width=506.0,
        height=59.0
    )

    canvas.create_text(
        349.0,
        214.0,
        anchor="nw",
        text="Chemin du Dockerfile :",
        fill="#FFFFFF",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        144.0,
        113.0,
        anchor="nw",
        text="Renseignez le chemin de l’image Docker (Dockerfile) de votre",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        134.0,
        141.0,
        anchor="nw",
        text="site prêt au déploiement en production pour l’intégrer au Honeypot.",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )
    window.mainloop()

def redirect_output(text_widget):
    class StdoutRedirector:
        def __init__(self, widget):
            self.widget = widget

        def write(self, output):
            self.widget.configure(state="normal")
            self.widget.insert("end", output)
            self.widget.see("end")
            self.widget.configure(state="disabled")

        def flush(self):
            pass

    sys.stdout = StdoutRedirector(text_widget)

def page7():
    if not is_dockerfile_path(page6_entry_1.get()):
        messagebox.showerror("Erreur.", "Chemin du Dockerfile invalide.")
        page6()

    canvas = Canvas(
        window,
        bg = "#003061",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets_page_4("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        431.0,
        288.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=53.0,
        y=95.0,
        width=756.0,
        height=384.0
    )

    canvas.create_rectangle(
        41.0,
        95.0,
        821.0,
        481.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        40.0,
        32.00000000000001,
        anchor="nw",
        text="Déploiement...",
        fill="#FCFCFC",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_rectangle(
        40.0,
        65.0,
        100.0,
        70.0,
        fill="#FCFCFC",
        outline="")
    
    button_image_1 = PhotoImage(
        file=relative_to_assets_page_6("button_1.png"))
    global button_1
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page8(),
        relief="flat"
    )
    button_1.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )
    button_1.pack()
    hide_button(button_1)

    # Rediriger la sortie standard vers le widget Text
    redirect_output(entry_1)

    install_thread = threading.Thread(target=install)
    install_thread.start()

    window.mainloop()

def page8():
    canvas = Canvas(
        window,
        bg = "#003061",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        431.0,
        0.0,
        862.0,
        519.0,
        fill="#FCFCFC",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets_page_7("image_1.png"))
    image_1 = canvas.create_image(
        646.0,
        199.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets_page_7("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat"
    )
    button_1.place(
        x=557.0,
        y=340.0,
        width=180.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_page_7("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_dashboard(),
        relief="flat"
    )
    button_2.place(
        x=557.0,
        y=408.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        93.0,
        209.0,
        anchor="nw",
        text="Configuration ",
        fill="#FCFCFC",
        font=("Roboto Bold", 40 * -1)
    )

    canvas.create_text(
        130.0,
        256.0,
        anchor="nw",
        text="terminée!",
        fill="#FCFCFC",
        font=("Roboto Bold", 40 * -1)
    )

    canvas.create_rectangle(
        186.0,
        312.0,
        246.0,
        317.0,
        fill="#FCFCFC",
        outline="")
    window.mainloop()

def open_dashboard():
    url = "http://localhost:3000"
    webbrowser.open(url)


def hide_button(widget):
    # This will remove the widget from toplevel
    widget.pack_forget()
  
# Method to make Button(widget) visible
def show_button(widget):
    # This will recover the widget from toplevel
    widget.pack()

def add_dockerfile_to_path(path):
    # Si le mot 'Dockerfile' n'est pas dans le chemin, l'ajoute à la fin
    if not path.endswith('Dockerfile'):
        path = os.path.join(path, 'Dockerfile')
    
    return path

def install():
    # Définir les options de configuration

    print('Creating config...')
    
    dockerfile = add_dockerfile_to_path(page6_entry_1.get())

    config = {
    "interface": page2_entry_2.get(),
    "subnet": page2_entry_1.get(),
    "dockerfile": dockerfile
    }

    if nofakemachine:
        config['dummy_pc'] = {
            'num_services': int(page3_entry_1.get()),
            'ip_addresses': [ip.strip() for ip in page3_entry_2.get().split(',')]
        }

    if noftp:
        config["ftp"] = {
            "ip_address": page4_entry_1.get(),
            "port": page4_entry_2.get()
        }

    # Créer le dossier 'build' s'il n'existe pas
    if not os.path.exists('build'):
        os.makedirs('build')

    # Path de la configuration
    config_file_path = "./build/config.json"

    # Écrire les options de configuration dans un fichier
    with open(config_file_path, 'w') as f:
        json.dump(config, f, indent=4)

    print('Launching Honeypot generator...')
    
    # Generer les docker compose en utilisant la configuration
    generate(config_file_path, page5_entry_2.get(), page5_entry_1.get())

    show_button(button_1)
    button_1.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )

page1()
