from tkinter import ttk
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PlotsView:
    def __init__(self, notebook, ledger):
        # Get main frame to work in it
        self.notebook = notebook

        # Get instance of class ledger
        self.ledger = ledger

        # Create self main frame
        self.plots_frame = ttk.Frame(
            master=self.notebook
        )
        self.plots_frame.pack(fill='both', expand=True)

    def display(self):
        # Content of the main frame
        header_lbl = ttk.Label(
            master=self.plots_frame,
            text="Visualization of finances",
            font=("Courier", 24, 'bold'),
        )
        header_lbl.pack(pady=20)

        self.refresh()
        # Return main frame
        return self.plots_frame

    def refresh(self):
        try:
            self.content_frame.pack_forget()
        except:
            pass
        self.content_frame = ttk.Frame(
            master=self.plots_frame
        )
        self.content_frame.pack()
        # Check if ledger is empty
        if(len(self.ledger.ledger) == 0):
            empty_ledger_lbl = ttk.Label(
                master=self.content_frame,
                text=self.ledger.get_ledger()
            )
            empty_ledger_lbl.pack()
        elif (len(self.ledger.ledger) == 1):
            empty_ledger_lbl = ttk.Label(
                master=self.content_frame,
                text="Not enough data in ledger to draw plots, add more deposits and withdrawals"
            )
            empty_ledger_lbl.pack()
        else:
            self.print_balance_plot()
            self.print_expenses_by_category_plot()

    def print_balance_plot(self):
        fig = Figure(figsize=(7, 4), dpi=100, facecolor='xkcd:charcoal grey',)
        fig.set_tight_layout('tight')
        fig.add_subplot(
            facecolor='grey',
        ).plot(
            self.ledger.get_ledger('index'),
            self.ledger.get_ledger('Balance'),
            color='g',
        )
        fig.suptitle('Balance', color='white', font="Consolas", fontsize=18)

        fig.supxlabel('No. operation', fontsize=10)
        fig.supylabel('Balance', fontsize=10)

        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, anchor=tk.N)

    def print_expenses_by_category_plot(self):
        fig = Figure(figsize=(4,4), dpi=100, facecolor='xkcd:charcoal grey',)
        fig.set_tight_layout('tight')
        fig.add_subplot(
            facecolor='grey',
        ).pie(
            self.ledger.get_expenses_by_category()['Amount'],
            labels=self.ledger.get_expenses_by_category().index,
            shadow=True,
            autopct='%1.1f%%',
        )
        fig.suptitle('Expenes by category', color='white', font="Consolas", fontsize=18)
        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, anchor=tk.N)