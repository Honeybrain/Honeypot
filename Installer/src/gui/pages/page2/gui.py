from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage, Entry, messagebox

from utils import is_valid_cidr, is_valid_interface

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page2():
    Page2()


class Page2(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg = "#003061",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.next_page(),
            relief="flat"
        )
        button_1.place(
            x=557.0,
            y=401.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_text(
            40.0,
            43.00000000000001,
            anchor="nw",
            text="Honeybrain setup :",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1)
        )

        self.canvas.create_rectangle(
            40.0,
            77.0,
            100.0,
            82.0,
            fill="#FCFCFC",
            outline="")

        self.canvas.create_text(
            40.0,
            388.0,
            anchor="nw",
            text="Configurez et déployez votre",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            417.0,
            anchor="nw",
            text="Honeypot depuis cet installateur sur",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            446.0,
            anchor="nw",
            text="votre site en production. ",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            98.0,
            anchor="nw",
            text="Honeybrain vise à détecter et attirer les ",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            127.0,
            anchor="nw",
            text="attaquants potentiels en simulant des",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            156.0,
            anchor="nw",
            text="services vulnérables, et grâce à son ",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            185.0,
            anchor="nw",
            text="dashboard d'administration et ses",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            214.0,
            anchor="nw",
            text="blocages d'IP automatisés, il permet ",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            243.0,
            anchor="nw",
            text="de surveiller les activités des attaquants",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            272.0,
            anchor="nw",
            text="et de bloquer les adresses IP",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            301.0,
            anchor="nw",
            text="suspectes pour renforcer la sécurité de",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            330.0,
            anchor="nw",
            text="de votre système.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            646.5,
            271.5,
            image=self.entry_image_1
        )
        self.page2_entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            fg="#000716",
            highlightthickness=0
        )
        self.page2_entry_1.insert('1', '192.168.1.0/24')
        self.page2_entry_1.place(
            x=486.0,
            y=241.0,
            width=321.0,
            height=59.0
        )

        self.canvas.create_text(
            475.0,
            213.0,
            anchor="nw",
            text="Sous réseau de votre réseau Honeypot :",
            fill="#FFFFFF",
            font=("Roboto Bold", 16 * -1)
        )

    def next_page(self):
        interface = "null"
        subnet = self.page2_entry_1.get()
        self.parent.data["interface"].set(interface)
        self.parent.data["subnet"].set(subnet)

        if not is_valid_cidr(subnet):
            messagebox.showerror("Erreur.", "Ceci n'est pas une adresse IP.")
        else:
            self.parent.change_page("page3")
