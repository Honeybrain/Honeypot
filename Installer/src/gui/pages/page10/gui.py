from pathlib import Path
from tkinter import Frame, Canvas, Button, PhotoImage, Entry, messagebox
import webbrowser

from utils import is_dockerfile_path, is_valid_email, is_valid_ip_list, is_valid_port

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page10():
    Page10()


class Page10(Frame):
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
            431.0, 0.0, 862.0, 519.0, fill="#FCFCFC", outline=""
        )

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(646.0, 199.0, image=self.image_image_1)

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: exit(),
            relief="flat",
        )
        self.button_1.place(x=557.0, y=340.0, width=180.0, height=55.0)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_dashboard(),
            relief="flat",
        )
        self.button_2.place(x=557.0, y=408.0, width=180.0, height=55.0)

        self.canvas.create_text(
            93.0,
            209.0,
            anchor="nw",
            text="Configuration ",
            fill="#FCFCFC",
            font=("Roboto Bold", 40 * -1),
        )

        self.canvas.create_text(
            130.0,
            256.0,
            anchor="nw",
            text="terminée!",
            fill="#FCFCFC",
            font=("Roboto Bold", 40 * -1),
        )

        self.canvas.create_rectangle(
            186.0, 312.0, 246.0, 317.0, fill="#FCFCFC", outline=""
        )

    def open_dashboard(self):
        url = "http://localhost:3000"
        webbrowser.open(url)
