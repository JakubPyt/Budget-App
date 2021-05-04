import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from notebook import NotebookView


class App:
    def __init__(self):
        # Create window
        self.window = ThemedTk(theme='equilux')
        self.window.title('Budget App')
        self.window.geometry("1000x500")

        # Content of window
        self.frame = ttk.Frame(
            master=self.window
        )
        self.display_welcome()
        self.frame.pack(fill='both', expand=True)

        self.window.mainloop()

    def display_welcome(self):
        header_lbl = ttk.Label(
            master=self.frame,
            text="Welcome in Budget App!",
            font=("Courier", 24, 'bold'),
        )
        header_lbl.pack(pady=20)
        subtitle_lbl = ttk.Label(
            master=self.frame,
            font=('Arial', 10, 'italic'),
            text="Your place to manage your finances!",
        )
        subtitle_lbl.pack(pady=10)
        you_can = ('You can:\n'
                   + '-Add deposits and withdrawals\n'
                   + '-Create a balance chart\n'
                   + '-Create a expenses by category chart\n')
        instructions_lbl = ttk.Label(
            master=self.frame,
            font=('Arial', 10),
            text=you_can,
            justify=tk.CENTER,
            padding=5
        )
        instructions_lbl.pack(pady=10)
        go_btn = ttk.Button(
            master=self.frame,
            text="Let's go!",
            command=self.cover_welcome
        )
        go_btn.pack()

    def cover_welcome(self):
        self.frame.pack_forget()
        NotebookView(self.window)
