from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage, Entry, messagebox

from utils import is_same_subnet, is_valid_cidr, is_valid_interface, is_valid_ip_list

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page3():
    Page3()


class Page3(Frame):
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
            0.0,
            862.0,
            519.0,
            fill="#FCFCFC",
            outline="")

        self.canvas.create_text(
            474.0,
            197.0,
            anchor="nw",
            text="(example: 192.168.1.16, 192.168.1.32) ",
            fill="#505485",
            font=("Roboto Bold", 14 * -1)
        )

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

        self.canvas.create_text(
            40.0,
            127.0,
            anchor="nw",
            text="Module fake machines",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1)
        )

        self.canvas.create_text(
            474.0,
            63.00000000000001,
            anchor="nw",
            text="Nombre de machines:",
            fill="#505485",
            font=("Roboto Bold", 16 * -1)
        )

        self.canvas.create_text(
            475.0,
            178.0,
            anchor="nw",
            text="IP spécifiques:",
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
            126.5,
            image=self.entry_image_1
        )
        self.page3_entry_1 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            fg="#000716",
            highlightthickness=0
        )
        self.page3_entry_1.place(
            x=486.0,
            y=96.0,
            width=321.0,
            height=59.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            646.5,
            271.5,
            image=self.entry_image_2
        )
        self.page3_entry_2 = Entry(
            self,
            bd=0,
            bg="#F1F5FF",
            fg="#000716",
            highlightthickness=0
        )
        self.page3_entry_2.place(
            x=486.0,
            y=241.0,
            width=321.0,
            height=59.0
        )

        self.canvas.create_text(
            40.0,
            186.0,
            anchor="nw",
            text="Générez de fausses machines à la",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            214.0,
            anchor="nw",
            text="volée ces machines seront visibles",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            242.0,
            anchor="nw",
            text="sur le réseau du honeypot pour",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            270.0,
            anchor="nw",
            text="simuler un environnement dans",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

        self.canvas.create_text(
            40.0,
            298.0,
            anchor="nw",
            text="une entreprise.",
            fill="#FCFCFC",
            font=("RobotoRoman Regular", 20 * -1)
        )

    def ignore(self):
        self.parent.data["nofakemachine"].set(True)
        self.parent.change_page("page4")

    def next_page(self):
        ip_addresses = self.page3_entry_2.get()
        num_services = self.page3_entry_1.get()
        subnet = self.parent.data["subnet"].get()
        self.parent.data["nofakemachine"].set(False)
        self.parent.data["ip_addresses"].set(ip_addresses)
        self.parent.data["num_services"].set(num_services)

        if not is_valid_ip_list(ip_addresses):
            messagebox.showerror("Erreur.", "Le format de la liste est invalide.")
        elif not is_same_subnet(ip_addresses):
            messagebox.showerror("Erreur.", "Au moins une IP n'est pas dans le sous réseau: " + subnet)
        else:
            self.parent.change_page("page4")