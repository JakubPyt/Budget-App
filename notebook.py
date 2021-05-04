from tkinter import ttk
from notebook_balance import BalanceView
from notebook_plots import PlotsView
from ledger import Ledger

class NotebookView:
    def __init__(self, window):
        # Create notebook
        notebook = ttk.Notebook(
            master=window,
            width=1000,
            height=500
        )

        # Create one instance of class ledger to sent it to BalanceView and PlotsView
        ledger = Ledger()

        # Create an instance of the class that get the mainframe to work in it
        bv = BalanceView(notebook, ledger)
        self.pv = PlotsView(notebook, ledger)

        # Pages of notebook display main frames from above classes
        notebook.add(bv.display(), text="Balance")
        notebook.add(self.pv.display(), text="Plots")
        notebook.bind("<<NotebookTabChanged>>", self.reload)
        # Display notebook
        notebook.pack()

    def reload(self, event):
        tab = event.widget.tab('current')['text']
        if tab == 'Plots':
            self.pv.refresh()