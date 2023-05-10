import tkinter as tk
from tkinter import ttk

class Installer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame

        self.show_frame(StartPage)
        self.geometry('800x600')
        self.resizable(False, False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=('Helvetica', 18, 'bold'))
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Next",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack(side="bottom", anchor='e')
        self.grid(row=0, column=0, sticky="nsew")

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=('Helvetica', 18, 'bold'))
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side="bottom", anchor='w')

        button2 = ttk.Button(self, text="Next",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(side="bottom", anchor='e')
        self.grid(row=0, column=0, sticky="nsew")

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two", font=('Helvetica', 18, 'bold'))
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack(side="bottom", anchor='w')
        self.grid(row=0, column=0, sticky="nsew")

app = Installer()
app.mainloop()