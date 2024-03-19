from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage, Entry, messagebox

from utils import is_valid_cidr, is_valid_interface

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page6():
    Page6()


class Page6(Frame):
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
            command=lambda: self.activate(),
            relief="flat"
        )
        button_1.place(
            x=557.0,
            y=300.0,
            width=180.0,
            height=55.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.desactivate(),
            relief="flat"
        )
        button_2.place(
            x=557.0,
            y=380.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_text(
            40.0,
            43.00000000000001,
            anchor="nw",
            text="Application mobile Honeybrain :",
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
            350.0,
            anchor="nw",
            text="Si vous souhaiter utiliser l’application",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            379.0,
            anchor="nw",
            text="mobile Honeybrain, vous devez activer",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            408.0,
            anchor="nw",
            text="le VPN Wireguard.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            98.0,
            anchor="nw",
            text="Honeybrain possède une application ",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            127.0,
            anchor="nw",
            text="mobile qui permet de visualiser les",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            156.0,
            anchor="nw",
            text="activités de votre Honeypot, grâce à son",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            185.0,
            anchor="nw",
            text="interface simple et intuitive.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            214.0,
            anchor="nw",
            text="L’application mobile Honeybrain permet",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            243.0,
            anchor="nw",
            text="de surveiller les attaques en temps réel.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            272.0,
            anchor="nw",
            text="Elle est disponible sur iOS et Android.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )


    def desactivate(self):
        self.parent.data["vpn"].set(False)
        self.parent.change_page("page7")

    def activate(self):
        self.parent.data["vpn"].set(True)
        self.parent.change_page("page7")