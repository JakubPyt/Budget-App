from tkinter import ttk
from ttkthemes import ThemedTk

class App:
    def __init__(self):
        self.window = ThemedTk(theme='equilux')
        self.window.title('Budget App')
        self.window.geometry('1000x500')
        self.welcome_label = ttk.Label(
            master=self.window,
            text='Hello World!'
        )
        self.welcome_label.pack()
        self.window.mainloop()
