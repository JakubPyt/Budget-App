import pandas as pd


class Ledger:
    def __init__(self):
        # Create empty ledger to storage information about balance
        self.ledger = pd.DataFrame(columns=['Amount', 'Balance', 'Description', 'Category'])

