from tkinter import ttk
import tkinter as tk

class BalanceView:
    def __init__(self, notebook, ledger):
        # Get main frame to work in it
        self.notebook = notebook

        # Get instance of class ledger
        self.ledger = ledger

        # Create self main frame
        self.balance_frame = ttk.Frame(
            master=self.notebook
        )
        self.balance_frame.pack(fill='both', expand=True)

    def display(self):
        # Content of the main frame
        # Header
        header_lbl = ttk.Label(
            master=self.balance_frame,
            text="Your ledger",
            font=("Courier", 24, 'bold'),
        )
        header_lbl.pack(pady=20)
        # Place for warnings
        self.warnings_lbl = ttk.Label(
            master=self.balance_frame,
            text='',
            foreground='red'
        )
        self.warnings_lbl.pack()


        # Return main frame
        return self.balance_frame

