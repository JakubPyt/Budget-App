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

        # Display "add" notebook
        self.print_add_nb()

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

    def print_add_nb(self):
        nb = ttk.Notebook(
            master=self.balance_frame,
            width=80,
            height=250
        )
        add_deposit_section = self.print_add_deposit(nb)
        nb.add(add_deposit_section, text="Add deposit")
        nb.pack(side=tk.LEFT, anchor=tk.N, padx=50, pady=10)

    # Functions for adding a deposit
    def print_add_deposit(self, notebook):
        # Frame
        add_deposit_frame = ttk.Frame(notebook)
        add_deposit_frame.pack(fill='both', expand=True)

        # Amount
        add_deposit_amount_lbl = ttk.Label(
            master=add_deposit_frame,
            text="Amount:"
        )
        add_deposit_amount_lbl.pack(pady=10)
        self.deposit_amount = tk.StringVar()
        self.add_deposit_amount_entry = ttk.Entry(
            master=add_deposit_frame,
            textvariable=self.deposit_amount
        )
        self.add_deposit_amount_entry.pack()

        # Description
        add_deposit_desc_lbl = ttk.Label(
            master=add_deposit_frame,
            text='Description:'
        )
        add_deposit_desc_lbl.pack(pady=10)
        self.deposit_desc = tk.StringVar()
        self.add_deposit_desc_entry = ttk.Entry(
            master=add_deposit_frame,
            textvariable=self.deposit_desc
        )
        self.add_deposit_desc_entry.pack()

        # Submit
        add_deposit_btn = ttk.Button(
            master=add_deposit_frame,
            text="Add...",
            command=self.add_deposit
        )
        add_deposit_btn.pack(pady=10)
        return add_deposit_frame
