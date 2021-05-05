from tkinter import ttk
from notebook_balance import BalanceView
from notebook_plots import PlotsView
from ledger import Ledger


class NotebookView:
    def __init__(self, window):
        # ==================
        # This(main) part of app is a notebook widget
        # ==================
        # Creating a notebook which will now be our main frame
        # This notebook will be sent to classes BalanceView and PlotsView
        notebook = ttk.Notebook(
            master=window,
            width=1000,
            height=500
        )

        # Create one instance of class ledger on which we will operate
        # This instance will be sent to classes BalanceView and PlotsView
        ledger = Ledger()

        # Create an instances of the classes to display them as a notebook pages
        bv = BalanceView(notebook, ledger)
        # We have self below to possibility to send this instance to method "reload"
        self.pv = PlotsView(notebook, ledger)

        # Add "display" methods from classes as pages
        notebook.add(bv.display(), text="Balance")
        notebook.add(self.pv.display(), text="Plots")

        # Bind notebook to method "reload"
        notebook.bind("<<NotebookTabChanged>>", self.reload)

        # Display notebook
        notebook.pack()

    def reload(self, event):
        """
        Method causes reload page "Plots".
        """
        # Check which tab is opened
        tab = event.widget.tab('current')['text']
        # If tab "Plots" is opened...
        if tab == 'Plots':
            # ... Call class method "display_content"
            # This method causes hide current screen with plots
            # And display plots with new data
            self.pv.display_content()
