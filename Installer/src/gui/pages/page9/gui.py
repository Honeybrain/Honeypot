import json
import os
from pathlib import Path
import sys
import threading
from tkinter import Frame, Canvas, Button, PhotoImage, Text, messagebox
from generator import generate

from utils import is_dockerfile_path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def page9():
    Page9()


class Page9(Frame):
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
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            431.0, 288.0, image=self.entry_image_1
        )
        self.entry_1 = Text(
            self, bd=0, bg="#F1F5FF", fg="#000716", highlightthickness=0
        )
        self.entry_1.place(x=53.0, y=95.0, width=756.0, height=384.0)

        self.canvas.create_rectangle(
            41.0, 95.0, 821.0, 481.0, fill="#FFFFFF", outline=""
        )

        self.canvas.create_text(
            40.0,
            32.00000000000001,
            anchor="nw",
            text="Déploiement...",
            fill="#FCFCFC",
            font=("Roboto Bold", 24 * -1),
        )

        self.canvas.create_rectangle(
            40.0, 65.0, 100.0, 70.0, fill="#FCFCFC", outline=""
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.next_page(),
            relief="flat",
        )
        self.button_1.place(x=557.0, y=401.0, width=180.0, height=55.0)
        self.button_1.pack()
        self.hide_button()

    def start(self):
        # Rediriger la sortie standard vers le widget Text
        self.redirect_output(self.entry_1)

        install_thread = threading.Thread(target=self.install)
        install_thread.start()

    def next_page(self):
        self.parent.change_page("page10")

    def redirect_output(self, text_widget):
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

    def remove_dockerfile_from_path(self, path):
        if path.endswith("Dockerfile"):
            path = os.path.dirname(path)

        return path

    def hide_button(self):
        # This will remove the widget from toplevel
        self.button_1.pack_forget()

    # Method to make Button(widget) visible
    def show_button(self):
        # This will recover the widget from toplevel
        self.button_1.pack()

    def install(self):
        # Définir les options de configuration

        print("[INFO] Creating config...")

        dockerfile = self.remove_dockerfile_from_path(
            self.parent.data["dockerfile"].get()
        )

        config = {
            "interface": self.parent.data["interface"].get(),
            "subnet": self.parent.data["subnet"].get(),
            "dockerfile": dockerfile,
        }

        if self.parent.data["nofakemachine"].get() == False:
            config["dummy_pc"] = {
                "num_services": int(self.parent.data["num_services"].get()),
                "ip_addresses": [
                    ip.strip()
                    for ip in self.parent.data["ip_addresses"].get().split(",")
                ],
            }

        if self.parent.data["noftp"].get() == False:
            config["ftp"] = {
                "ip_address": self.parent.data["ip_address"].get(),
                "port": self.parent.data["port"].get(),
            }

        # Créer le dossier 'build' s'il n'existe pas
        if not os.path.exists("../build"):
            os.makedirs("../build")

        # Path de la configuration
        config_file_path = "../build/config.json"

        # Écrire les options de configuration dans un fichier
        with open(config_file_path, "w") as f:
            json.dump(config, f, indent=4)

        print("[ OK ] Config created.")

        print("[INFO] Launching Honeypot generator...")

        # Generer les docker compose en utilisant la configuration
        generate(
            config_file_path,
            self.parent.data["mail"].get(),
            self.parent.data["password"].get(),
        )

        self.show_button()
        self.button_1.place(x=557.0, y=401.0, width=180.0, height=55.0)
