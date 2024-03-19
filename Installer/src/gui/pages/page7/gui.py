from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage, Entry, messagebox

from utils import is_valid_email, is_valid_ip_list, is_valid_port

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page7():
    Page7()


class Page7(Frame):
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
            258.0,
            61.00000000000001,
            anchor="nw",
            text="on y est presque ...",
            fill="#FCFCFC",
            font=("Roboto Bold", 40 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            430.5,
            329.5,
            image=self.entry_image_1
        )
        self.page7_entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            fg="#000716",
            highlightthickness=0
        )
        self.page7_entry_1.place(
            x=278.0,
            y=299.0,
            width=305.0,
            height=59.0
        )

        self.canvas.create_text(
            266.0,
            275.0,
            anchor="nw",
            text="Mot de passe :",
            fill="#FFFFFF",
            font=("Roboto Bold", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            430.5,
            231.5,
            image=self.entry_image_2
        )
        self.page7_entry_2 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            fg="#000716",
            highlightthickness=0
        )
        self.page7_entry_2.place(
            x=278.0,
            y=201.0,
            width=305.0,
            height=59.0
        )

        self.canvas.create_text(
            266.0,
            177.0,
            anchor="nw",
            text="E-mail :",
            fill="#FFFFFF",
            font=("Roboto Bold", 16 * -1)
        )

        self.canvas.create_text(
            149.0,
            113.0,
            anchor="nw",
            text="Créez votre compte administrateur pour accéder au dashboard",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            274.0,
            141.0,
            anchor="nw",
            text="d’administration de votre honeypot.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

    def next_page(self):
        mail = self.page7_entry_2.get()
        password = self.page7_entry_1.get()
        self.parent.data["mail"].set(mail)
        self.parent.data["password"].set(password)

        if not is_valid_email(mail):
            messagebox.showerror("Erreur.", "E-mail invalide.")
        else:
            self.parent.change_page("page8")