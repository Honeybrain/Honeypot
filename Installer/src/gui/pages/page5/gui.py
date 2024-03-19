from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage, Entry, messagebox

from utils import is_valid_ip_list, is_valid_port

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page5():
    Page5()


class Page5(Frame):
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
        self.canvas.create_rectangle(
            431.0,
            7.105427357601002e-15,
            866.0,
            519.0,
            fill="#FCFCFC",
            outline="")

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
            40.0,
            127.0,
            anchor="nw",
            text="Module fausse base de données",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1)
        )

        self.canvas.create_text(
            474.0,
            90.0,
            anchor="nw",
            text="Adresse IP de la base de données:",
            fill="#505485",
            font=("Roboto Bold", 16 * -1)
        )

        self.canvas.create_text(
            474.0,
            207.0,
            anchor="nw",
            text="Port de la base de donnée:",
            fill="#505485",
            font=("Roboto Bold", 16 * -1)
        )

        self.canvas.create_rectangle(
            40.0,
            160.0,
            100.0,
            165.0,
            fill="#FCFCFC",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            646.5,
            153.5,
            image=self.entry_image_1
        )
        self.page5_entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            fg="#000716",
            highlightthickness=0
        )
        self.page5_entry_1.place(
            x=486.0,
            y=123.0,
            width=321.0,
            height=59.0
        )

        self.canvas.create_text(
            40.0,
            186.0,
            anchor="nw",
            text="Générez une fausse base de données",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            214.0,
            anchor="nw",
            text="accessible sur l'adresse IP que vous",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            242.0,
            anchor="nw",
            text="voulez et sur le port que vous voulez,",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            270.0,
            anchor="nw",
            text="pour attirer l’attaquant et collecter",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            299.0,
            anchor="nw",
            text="le maximum d’informations sur lui.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )


        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.ignore(),
            relief="flat"
        )
        self.button_2.place(
            x=557.0,
            y=331.0,
            width=180.0,
            height=55.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            646.5,
            271.5,
            image=self.entry_image_2
        )
        self.page5_entry_2 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            fg="#000716",
            highlightthickness=0
        )
        self.page5_entry_2.insert('1', '21')
        self.page5_entry_2.place(
            x=486.0,
            y=241.0,
            width=321.0,
            height=59.0
        )

    def ignore(self):
        self.parent.data["fakedb"].set(False)
        self.parent.change_page("page6")

    def next_page(self):
        ip_address = self.page5_entry_1.get()
        port = self.page5_entry_2.get()
        self.parent.data["fakedb"].set(True)
        self.parent.data["db_ip_address"].set(ip_address)
        self.parent.data["db_port"].set(port)

        if not is_valid_ip_list(ip_address):
            messagebox.showerror("Erreur.", "Adresse IP invalide.")
        elif not is_valid_port(port):
            messagebox.showerror("Erreur.", "Port invalide.")
        else:
            self.parent.change_page("page6")