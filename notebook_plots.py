from tkinter import ttk


class PlotsView:
    def __init__(self, notebook):
        # Get main frame to work in it
        self.notebook = notebook

    def display(self):
        # Create self main frame
        plots_frame = ttk.Frame(
            master=self.notebook
        )
        plots_frame.pack(fill='both', expand=True)

        # Content of the main frame
        welcome_lbl = ttk.Label(
            master=plots_frame,
            text="Hello from plots"
        )
        welcome_lbl.pack()

        # Return main frame
        return plots_frame
