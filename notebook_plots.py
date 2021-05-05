from tkinter import ttk
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PlotsView:
    def __init__(self, notebook, ledger):
        # Get instance of class ledger
        self.ledger_instance = ledger

        # Create self main frame to work in it
        self.plots_frame = ttk.Frame(
            master=notebook,
        )
        self.plots_frame.pack(fill='both', expand=True)

    def display(self):
        """
        Method to display component.
        :return: plots_frame(ttk.Frame)
        """
        # Header of the component
        header_lbl = ttk.Label(
            master=self.plots_frame,
            text="Visualization of finances",
            font=("Courier", 24, 'bold'),
        )
        header_lbl.pack(pady=20)

        # Method which display content of component
        self.display_content()

        # Return main frame
        return self.plots_frame

    def display_content(self):
        """
        Method to display and refresh(with new data) content of component.
        """
        # ======================
        # Try to delete current content of component(if exist)
        # ======================
        try:
            self.content_frame.pack_forget()
        except:
            pass
        # ======================
        # Build new content of component
        # ======================
        # In this frame we will have content of component
        self.content_frame = ttk.Frame(
            master=self.plots_frame
        )
        self.content_frame.pack()

        # Display according to length of ledger
        if len(self.ledger_instance.ledger) == 0:
            # If ledger is empty, we can use str which is returned
            # from get_ledger() method to inform user to add deposits and withdrawals
            empty_ledger_lbl = ttk.Label(
                master=self.content_frame,
                text=self.ledger_instance.get_ledger()
            )
            empty_ledger_lbl.pack()
        elif len(self.ledger_instance.ledger) == 1:
            # If in ledger is less 2 entries, plots not look to good
            # So we create label to add more deposits and withdrawals
            empty_ledger_lbl = ttk.Label(
                master=self.content_frame,
                text="Not enough data in ledger to draw plots, add more deposits and withdrawals"
            )
            empty_ledger_lbl.pack()
        else:
            # If in ledger is at least 2 entries,
            # We can call methods which draw plots
            self.print_balance_plot()
            self.print_expenses_by_category_plot()

    def print_balance_plot(self):
        """
        Method displays plot with balance against the operation number.
        """
        # ======================
        # Create figure for plot
        # ======================
        # Create figure
        fig = Figure(
            figsize=(7, 4),
            dpi=100,
            facecolor='xkcd:charcoal grey',
        )

        # Set paddings inside figure
        fig.set_tight_layout('tight')

        # Create plot
        fig.add_subplot(
            facecolor='grey',
        ).plot(
            self.ledger_instance.get_ledger('index'),  # Indexes of operations
            self.ledger_instance.get_ledger('Balance'),  # Balance after each operation
            color='g',
        )

        # Style of header of plot
        fig.suptitle(
            'Balance',
            color='white',
            font="Consolas",
            fontsize=18
        )

        # Set titles for labels
        fig.supxlabel('No. operation', fontsize=10)
        fig.supylabel('Balance', fontsize=10)

        # ======================
        # Create canvas on which figure(plot) will be displayed
        # ======================
        # Create canvas
        canvas = FigureCanvasTkAgg(
            fig,  # Point the figure to display
            master=self.content_frame  # Indicate the frame in which it is to be displayed
        )
        canvas.draw()

        # Location of canvas
        canvas.get_tk_widget().pack(side=tk.LEFT, anchor=tk.N)

    def print_expenses_by_category_plot(self):
        """
        Method displays pie chart with expenses by category.
        """
        # ======================
        # Create figure for plot
        # ======================
        # Create figure
        fig = Figure(
            figsize=(4, 4),
            dpi=100,
            facecolor='xkcd:charcoal grey',
        )

        # Set paddings inside figure
        fig.set_tight_layout('tight')

        # Create plot
        fig.add_subplot(
            facecolor='grey',
        ).pie(
            self.ledger_instance.get_expenses_by_category()['Amount'],  # Sum by category
            labels=self.ledger_instance.get_expenses_by_category().index,  # Names of categories
            shadow=True,  # Shadow under the pies
            autopct='%1.1f%%',  # Format of values on pies
        )

        # Style of header of plot
        fig.suptitle(
            'Expenes by category',
            color='white',
            font="Consolas",
            fontsize=18
        )

        # ======================
        # Create canvas on which figure(pie chart) will be displayed
        # ======================
        # Create canvas
        canvas = FigureCanvasTkAgg(
            fig,  # Point the figure to display
            master=self.content_frame  # Indicate the frame in which it is to be displayed
        )
        canvas.draw()

        # Location of canvas
        canvas.get_tk_widget().pack(side=tk.LEFT, anchor=tk.N)
