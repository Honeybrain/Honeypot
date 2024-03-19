from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page1():
    Page1()


class Page1(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#003061",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            430.9999999999999, 0.0, 861.9999999999999, 519.0, fill="#FCFCFC", outline=""
        )

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.image_1 = self.canvas.create_image(
            645.9999999999999, 237.0, image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.change_page("page2"),
            relief="flat",
        )
        button_1.place(x=556.9999999999999, y=401.0, width=180.0, height=55.0)

        self.canvas.create_text(
            39.999999999999886,
            127.0,
            anchor="nw",
            text="Bienvenue sur Honeybrain",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1),
        )

        self.canvas.create_rectangle(
            39.999999999999886,
            160.0,
            99.99999999999989,
            165.0,
            fill="#FCFCFC",
            outline="",
        )

        self.canvas.create_text(
            39.999999999999886,
            186.0,
            anchor="nw",
            text="Sécurisez vos projets en déployant",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1),
        )

        self.canvas.create_text(
            39.999999999999886,
            214.0,
            anchor="nw",
            text="notre solution tout-en-un !",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1),
        )

        self.canvas.create_text(
            39.999999999999886,
            214.0,
            anchor="nw",
            text="notre solution tout-en-un !",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1),
        )

        self.canvas.create_text(
            39.999999999999886,
            242.0,
            anchor="nw",
            text="Détectez les attaques grâce",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1),
        )

        self.canvas.create_text(
            39.999999999999886,
            270.0,
            anchor="nw",
            text="à notre honeypot facile à installer et",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1),
        )

        self.canvas.create_text(
            39.999999999999886,
            298.0,
            anchor="nw",
            text="et protégez votre site internet.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1),
        )
