from tkinter import ttk
from notebook_balance import BalanceView
from notebook_plots import PlotsView


class NotebookView:
    def __init__(self, window):
        # Create notebook
        notebook = ttk.Notebook(
            master=window,
            width=1000,
            height=500
        )

        # Create an instance of the class that get the mainframe to work in it
        bv = BalanceView(notebook)
        pv = PlotsView(notebook)

        # Pages of notebook display main frames from above classes
        notebook.add(bv.display(), text="Balance")
        notebook.add(pv.display(), text="Plots")

        # Display notebook
        notebook.pack()
