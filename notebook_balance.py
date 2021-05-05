from tkinter import ttk
import tkinter as tk


class BalanceView:
    def __init__(self, notebook, ledger):
        # Get instance of class ledger
        self.ledger_instance = ledger

        # Create self main frame
        self.balance_frame = ttk.Frame(
            master=notebook
        )
        self.balance_frame.pack(fill='both', expand=True)

    def display(self):
        """
        Main method to display component.
        :return: balance_frame(ttk.Frame)
        """

        # Header of the component
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

        # ======================
        # Content of the component
        # ======================

        # Display "add" notebook
        self.print_add_nb()

        # Display table
        self.print_table()

        # Return main frame
        return self.balance_frame

    def print_table(self):
        """
        Method to display and refresh(with new data) table.
        :return: None
        """
        # When method is called, it refresh table(delete old and build new with new data)
        # Try to delete current text widget(if exist)
        try:
            self.place_for_table_txt.pack_forget()
        except:
            pass

        # Table is inside tk.Text widget
        # Build new text widget
        self.place_for_table_txt = tk.Text(
            master=self.balance_frame,
            width=100,
            height=100,
            padx=10,
            pady=10,
            bg='light grey'
        )

        # Insert table from .get_ledger method into text widget
        self.place_for_table_txt.insert(tk.END, str(self.ledger_instance.get_ledger()))

        # Set configuration for text widget
        self.place_for_table_txt.config(
            state='disabled',  # Disable for editing
            xscrollcommand=True  # If there are to many rows in table, enable scroll
        )

        # Location of table
        self.place_for_table_txt.pack(side=tk.RIGHT, anchor=tk.N, padx=10, pady=10)

    def print_add_nb(self):
        """
        Method display notebook in which there are pages to add deposits and withdrawals.
        :return: None
        """
        # Create notebook
        nb = ttk.Notebook(
            master=self.balance_frame,
            width=80,
            height=250
        )

        # Methods below return frames with appropriate sections
        add_deposit_section = self.print_add_deposit(nb)
        add_withdrawal_section = self.print_add_withdrawal(nb)

        # Add pages to notebook
        nb.add(add_deposit_section, text="Add deposit")
        nb.add(add_withdrawal_section, text="Add withdrawal")

        # Location of notebook
        nb.pack(side=tk.LEFT, anchor=tk.N, padx=50, pady=10)

    def print_add_deposit(self, notebook):
        """
        Method build section to add deposits to ledger.
        :param notebook: ttk.Frame
        :return: add_deposit_frame(ttk.Frame)
        """

        # Create main frame of this section
        add_deposit_frame = ttk.Frame(notebook)
        add_deposit_frame.pack(fill='both', expand=True)

        # ======================
        # Amount - label + entry
        # ======================
        add_deposit_amount_lbl = ttk.Label(
            master=add_deposit_frame,
            text="Amount:"
        )
        add_deposit_amount_lbl.pack(pady=10)

        # Var below will be read in add_deposit method
        self.deposit_amount = tk.StringVar()

        # This entry will be cleared in add_deposit method
        self.add_deposit_amount_entry = ttk.Entry(
            master=add_deposit_frame,
            textvariable=self.deposit_amount  # Connect this entry with string above
        )
        self.add_deposit_amount_entry.pack()

        # ======================
        # Description - label + entry
        # ======================
        add_deposit_desc_lbl = ttk.Label(
            master=add_deposit_frame,
            text='Description:'
        )
        add_deposit_desc_lbl.pack(pady=10)

        # Var below will be read in add_deposit method
        self.deposit_desc = tk.StringVar()

        # This entry will be cleared in add_deposit method
        self.add_deposit_desc_entry = ttk.Entry(
            master=add_deposit_frame,
            textvariable=self.deposit_desc  # Connect this entry with string above
        )
        self.add_deposit_desc_entry.pack()

        # Submit button
        add_deposit_btn = ttk.Button(
            master=add_deposit_frame,
            text="Add...",
            command=self.add_deposit  # Click call add_deposit method
        )
        add_deposit_btn.pack(pady=10)

        # Return to display
        return add_deposit_frame

    def add_deposit(self):
        """
        Method adds deposit to ledger by calling 'ledger.add_deposit' method.
        :return: None
        """
        # Checking if the data is correct
        try:
            # Try to get data from self.deposit_amount from print_add_deposit
            d_amount = float(self.deposit_amount.get())

            # Clearing warnings label
            self.warnings_lbl.configure(text="")
        except:
            try:
                # Try to replace ',' to '.' and then get value
                d_amount = float(self.deposit_amount.get().replace(',', '.'))

                # Clearing warnings label
                self.warnings_lbl.configure(text="")
            except:
                if self.deposit_amount.get() != '':
                    # If methods above not working, print info for user
                    self.warnings_lbl.configure(text="Only digits in amount")

        # Get describe from self.deposit_desc from print_add_deposit
        d_desc = self.deposit_desc.get()

        # Add amount and description to ledger
        self.ledger_instance.add_deposit(d_amount, d_desc)

        # Reload table(with new data)
        self.print_table()

        # Clear entries in print_add_deposit
        self.add_deposit_amount_entry.delete(0, 'end')
        self.add_deposit_desc_entry.delete(0, 'end')

    def print_add_withdrawal(self, notebook):
        """
        Method build section to add withdrawals to ledger.
        :param notebook: ttk.Frame
        :return: add_withdrawal_frame(ttk.Frame)
        """

        # Create main frame of this section
        add_withdrawal_frame = ttk.Frame(notebook)
        add_withdrawal_frame.pack(fill='both', expand=True)

        # ======================
        # Amount - label + entry
        # ======================
        add_withdrawal_amount_lbl = ttk.Label(
            master=add_withdrawal_frame,
            text="Amount:"
        )
        add_withdrawal_amount_lbl.pack(pady=10)

        # Var below will be read in add_withdrawal method
        self.withdrawal_amount = tk.StringVar()

        # This entry will be cleared in add_withdrawal method
        self.add_withdrawal_amount_entry = ttk.Entry(
            master=add_withdrawal_frame,
            textvariable=self.withdrawal_amount  # Connect this entry with string above
        )
        self.add_withdrawal_amount_entry.pack()

        # ======================
        # Category - label + option menu
        # ======================
        add_withdrawal_category_lbl = ttk.Label(
            master=add_withdrawal_frame,
            text="Category:"
        )
        add_withdrawal_category_lbl.pack(pady=10)

        # Category options will be read in add_withdrawal method
        self.options = ['Unsigned', 'Car', 'Food', 'Child', 'Taxes', 'Unsigned']

        # Var below will be read in add_withdrawal method
        self.withdrawal_category = tk.StringVar()

        # Option menu allows to select a category
        add_withdrawal_category_om = ttk.OptionMenu(
            add_withdrawal_frame,
            self.withdrawal_category,
            *self.options
        )
        add_withdrawal_category_om.pack()

        # ======================
        # Description - label + entry
        # ======================
        add_withdrawal_desc_lbl = ttk.Label(
            master=add_withdrawal_frame,
            text='Description:'
        )
        add_withdrawal_desc_lbl.pack(pady=10)

        # Var below will be read in add_withdrawal method
        self.withdrawal_desc = tk.StringVar()

        # This entry will be cleared in add_withdrawal method
        self.add_withdrawal_desc_entry = ttk.Entry(
            master=add_withdrawal_frame,
            textvariable=self.withdrawal_desc
        )
        self.add_withdrawal_desc_entry.pack()

        # Submit button
        add_withdrawal_btn = ttk.Button(
            master=add_withdrawal_frame,
            text="Add...",
            command=self.add_withdrawal  # Click call add_withdrawal func
        )
        add_withdrawal_btn.pack(pady=10)

        # Return to display
        return add_withdrawal_frame

    def add_withdrawal(self):
        """
        Method adds withdrawal to ledger by calling 'ledger.add_withdrawal' method.
        :return: None
        """
        # Checking if the data is correct
        try:
            # Try to get data from self.withdrawal_amount from print_add_withdrawal
            w_amount = float(self.withdrawal_amount.get())

            # Clearing warnings label
            self.warnings_lbl.configure(text="")
        except:
            try:
                # Try to replace ',' to '.' and then get value
                w_amount = float(self.withdrawal_amount.get().replace(',','.'))

                # Clearing warnings label
                self.warnings_lbl.configure(text="")
            except:
                if self.withdrawal_amount.get() != '':
                    # If methods above not working, print info for user
                    self.warnings_lbl.configure(text="Only digits in amount")

        # Get describe and category from them vars in print_add_deposit
        w_category = self.withdrawal_category.get()
        w_desc = self.withdrawal_desc.get()

        # Add amount, description and category to ledger
        # If user doesn't have enough funds to perform operation
        # ledger.add_withdrawal method will return False
        # And then, warning will be displayed
        w_result = self.ledger_instance.add_withdrawal(w_amount, w_desc, w_category)
        if w_result == False:
            self.warnings_lbl.configure(text="You don't have enough funds in your account")

        # Reload table(with new data)
        self.print_table()

        # Clear entries in print_add_withdrawal
        self.add_withdrawal_amount_entry.delete(0, 'end')
        self.add_withdrawal_desc_entry.delete(0, 'end')
        self.withdrawal_category.set(self.options[0])