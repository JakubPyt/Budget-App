from tkinter import ttk
from ttkthemes import ThemedTk
from notebook import NotebookView

class App:
    def __init__(self):
        self.window = ThemedTk(theme='equilux')
        self.window.title('Budget App')
        self.window.geometry('1000x500')
        notebook = NotebookView(self.window)

        self.window.mainloop()
