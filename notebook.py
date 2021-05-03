from tkinter import ttk

class NotebookView:
    def __init__(self, window):
        self.window = window
        self.welcome_label = ttk.Label(
            master=self.window,
            text='Hello World!'
        )
        self.welcome_label.pack()