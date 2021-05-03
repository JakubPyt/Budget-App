from tkinter import ttk
from ttkthemes import ThemedTk
from notebook import NotebookView

class App:
    def __init__(self):
        # Create window
        self.window = ThemedTk(theme='equilux')
        self.window.title('Budget App')

        # Content of window
        notebook = NotebookView(self.window)

        #
        self.window.mainloop()
