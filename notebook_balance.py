from tkinter import ttk


class BalanceView:
    def __init__(self, notebook):
        # Get main frame to work in it
        self.notebook = notebook

    def display(self):
        # Create self main frame
        balance_frame = ttk.Frame(
            master=self.notebook
        )
        balance_frame.pack(fill='both', expand=True)

        # Content of the main frame
        welcome_lbl = ttk.Label(
            master=balance_frame,
            text="Hello from balance"
        )
        welcome_lbl.pack()

        # Return main frame
        return balance_frame
