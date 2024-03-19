from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage, Entry, messagebox

from utils import is_dockerfile_path, is_valid_email, is_valid_ip_list, is_valid_port

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page8():
    Page8()


class Page8(Frame):
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
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.next_page(),
            relief="flat"
        )
        self.button_1.place(
            x=557.0,
            y=401.0,
            width=180.0,
            height=55.0
        )

        self.canvas.create_text(
            252.0,
            61.00000000000001,
            anchor="nw",
            text="une dernière étape !",
            fill="#FCFCFC",
            font=("Roboto Bold", 40 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            431.0,
            274.5,
            image=self.entry_image_1
        )
        self.page8_entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            fg="#000716",
            highlightthickness=0
        )
        self.page8_entry_1.place(
            x=178.0,
            y=244.0,
            width=506.0,
            height=59.0
        )

        self.canvas.create_text(
            349.0,
            214.0,
            anchor="nw",
            text="Chemin du Dockerfile :",
            fill="#FFFFFF",
            font=("Roboto Bold", 16 * -1)
        )

        self.canvas.create_text(
            144.0,
            113.0,
            anchor="nw",
            text="Renseignez le chemin de l’image Docker (Dockerfile) de votre",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            134.0,
            141.0,
            anchor="nw",
            text="site prêt au déploiement en production pour l’intégrer au Honeypot.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

    def next_page(self):
        dockerfile = self.page8_entry_1.get()
        self.parent.data["dockerfile"].set(dockerfile)

        if not is_dockerfile_path(dockerfile):
            messagebox.showerror("Erreur.", "Chemin du Dockerfile invalide.")
        else:
            self.parent.change_page("page9")