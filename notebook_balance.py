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


        # Display table
        self.print_table()

        # Return main frame
        return self.balance_frame

    def print_table(self):
        try:
            self.place_for_table_txt.pack_forget()
        except:
            pass
        self.place_for_table_txt = tk.Text(
            master=self.balance_frame,
            width=100,
            height=100,
            padx=10,
            pady=10
        )
        self.place_for_table_txt.insert(tk.END, str(self.ledger.get_ledger()))
        self.place_for_table_txt.pack(side=tk.RIGHT, anchor=tk.N, padx=10, pady=10)

