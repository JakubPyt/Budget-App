# Import pretty looks elements
from tkinter import ttk
# Above elements will have theme from this import
from ttkthemes import ThemedTk
# Import other elements(which are not in above module)
import tkinter as tk
# Import next screen of app(file: notebook.py)
from notebook import NotebookView


class App:
    def __init__(self):
        # Create window
        self.window = ThemedTk(theme='black')  # Choose theme
        self.window.title('Budget App')  # Title of app
        self.window.geometry("1000x500")  # Width x height of app window

        # ======================
        # Content of this window
        # ======================
        # Create main frame for this view
        self.welcome_frame = ttk.Frame(master=self.window)
        self.welcome_frame.pack(fill='both', expand=True)
        # Call function that displays content of this view
        self.display_welcome()

        # Run window
        self.window.mainloop()

    def display_welcome(self):
        """
        Function displays welcome view.
        """
        # Header of this view
        header_lbl = ttk.Label(  # Define element
            master=self.welcome_frame,  # In which element is to be displayed
            text="Welcome in Budget App!",
            font=("Courier", 24, 'bold'),
        )
        header_lbl.pack(pady=20)  # Display element

        # Subtitle of this view
        subtitle_lbl = ttk.Label(
            master=self.welcome_frame,
            text="Your place to manage your finances!",
        )
        subtitle_lbl.pack(pady=10)

        # Description of the application
        you_can = ('You can here:\n'
                   + '-Add deposits and withdrawals\n'
                   + '-Create a balance chart\n'
                   + '-Create a expenses by category chart\n')
        description_lbl = ttk.Label(
            master=self.welcome_frame,
            text=you_can,
            justify=tk.CENTER,
            padding=5
        )
        description_lbl.pack(pady=10)

        # Button to run main part of app
        start_btn = ttk.Button(
            master=self.welcome_frame,
            text="Let's go!",
            padding=10,
            command=self.hide_welcome  # When click, go to func
        )
        start_btn.pack()

    def hide_welcome(self):
        """
        Function hide welcome view and run notebook(main part of app).
        """
        # Hide this view
        self.welcome_frame.pack_forget()
        # Run notebook
        NotebookView(self.window)
