
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from generator import generate
import json
import os
import sys
import threading

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

ASSETS_PATH_PAGE_5 = OUTPUT_PATH / Path(r"assets/frame1")
def relative_to_assets_page_5(path: str) -> Path:
    return ASSETS_PATH_PAGE_5 / Path(path)

window = Tk()

window.geometry("862x519")
window.configure(bg = "#003061")

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

    button_image_1 = PhotoImage(
        file=relative_to_assets_page_1("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=556.9999999999999,
        y=401.0,
        width=180.0,
        height=55.0
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
        text="Tutoriel général:",
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
        253.0,
        anchor="nw",
        text="Configurez et déployez votre Honeypot depuis cet installateur sur votre site",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        282.0,
        anchor="nw",
        text="en production. ",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        98.0,
        anchor="nw",
        text="Honeybrain vise à détecter et attirer les attaquants potentiels en simulant des",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        127.0,
        anchor="nw",
        text="services vulnérables, et grâce à son dashboard d'administration",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        156.0,
        anchor="nw",
        text="et ses blocages d'IP automatisés, il permet de surveiller les activités des",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        185.0,
        anchor="nw",
        text="attaquants et de bloquer les adresses IP suspectes pour renforcer la sécurité",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        214.0,
        anchor="nw",
        text="de votre système.",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets_page_2("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        216.5,
        428.5,
        image=entry_image_1
    )
    global page2_entry_1
    page2_entry_1 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page2_entry_1.place(
        x=56.0,
        y=398.0,
        width=321.0,
        height=59.0
    )

    canvas.create_text(
        50.0,
        351.0,
        anchor="nw",
        text="Sous réseau de votre réseau Honeypot :",
        fill="#FFFFFF",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        50.0,
        370.0,
        anchor="nw",
        text="(exemple : 192.168.1.0/24)",
        fill="#FFFFFF",
        font=("Roboto Bold", 14 * -1)
    )

    window.mainloop()

def page3():
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
        478.0,
        242.0,
        anchor="nw",
        text="(séparé par des virgules: 192.168.1.16, 192.168.1.32) ",
        fill="#505485",
        font=("Roboto Bold", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets_page_3("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page4(),
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
        text="Module fake machines",
        fill="#FCFCFC",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_text(
        478.0,
        108.0,
        anchor="nw",
        text="Nombre de machines:",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        479.0,
        223.0,
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
        650.5,
        171.5,
        image=entry_image_1
    )
    global page3_entry_1
    page3_entry_1 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page3_entry_1.place(
        x=490.0,
        y=141.0,
        width=321.0,
        height=59.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets_page_3("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        650.5,
        312.5,
        image=entry_image_2
    )
    global page3_entry_2
    page3_entry_2 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page3_entry_2.place(
        x=490.0,
        y=282.0,
        width=321.0,
        height=59.0
    )

    canvas.create_text(
        40.0,
        186.0,
        anchor="nw",
        text="Générez de fausses machines à la volée,",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        214.0,
        anchor="nw",
        text="ces machines seront visibles sur le",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        242.0,
        anchor="nw",
        text="réseau du honeypot pour simuler",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas.create_text(
        40.0,
        270.0,
        anchor="nw",
        text="un environnement dans une entreprise.",
        fill="#FCFCFC",
        font=("RobotoRoman Regular", 20 * -1)
    )
    window.mainloop()

def page4():
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
        435.0,
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
        command=lambda: page5(),
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
        478.0,
        136.0,
        anchor="nw",
        text="Adresse IP du serveur:",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        478.0,
        245.0,
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
        650.5,
        199.5,
        image=entry_image_1
    )
    global page4_entry_1
    page4_entry_1 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page4_entry_1.place(
        x=490.0,
        y=169.0,
        width=321.0,
        height=59.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets_page_3("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        650.5,
        308.5,
        image=entry_image_2
    )
    global page4_entry_2
    page4_entry_2 = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    page4_entry_2.place(
        x=490.0,
        y=278.0,
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

def page5():
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
    # Rediriger la sortie standard vers le widget Text
    redirect_output(entry_1)

    install_thread = threading.Thread(target=install)
    install_thread.start()

    window.mainloop()

def page6():
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
        file=relative_to_assets_page_5("image_1.png"))
    image_1 = canvas.create_image(
        646.0,
        237.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets_page_5("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_page_5("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: install(),
        relief="flat"
    )
    button_2.place(
        x=557.0,
        y=401.0,
        width=180.0,
        height=55.0
    )

    canvas.create_text(
        94.0,
        183.0,
        anchor="nw",
        text="Configuration ",
        fill="#FCFCFC",
        font=("Roboto Bold", 40 * -1)
    )

    canvas.create_text(
        118.0,
        230.0,
        anchor="nw",
        text="terminée!",
        fill="#FCFCFC",
        font=("Roboto Bold", 40 * -1)
    )

    canvas.create_rectangle(
        144.0,
        286.0,
        204.0,
        291.0,
        fill="#FCFCFC",
        outline="")
    window.mainloop()

def install():
    # Définir les options de configuration

    print('Creating config...')

    config = {
        'dummy_pc': {
            'num_services': int(page3_entry_1.get()),
            'ip_addresses': [ip.strip() for ip in page3_entry_2.get().split(',')]
        },
        "ftp": {
            "ip_address": page4_entry_1.get(),
            "port": page4_entry_2.get()
        },
        "subnet": page2_entry_1.get()
    }

    # Créer le dossier 'build' s'il n'existe pas
    if not os.path.exists('build'):
        os.makedirs('build')

    # Path de la configuration
    config_file_path = "./build/config.json"

    # Écrire les options de configuration dans un fichier
    with open(config_file_path, 'w') as f:
        json.dump(config, f, indent=4)
    
    # Generer les docker compose en utilisant la configuration
    generate(config_file_path)
    
page1()
