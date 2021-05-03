import pandas as pd


class Ledger:
    def __init__(self):
        # Create empty ledger to storage information about balance
        self.ledger = pd.DataFrame(columns=['Amount', 'Balance', 'Description', 'Category'])

    # Func add deposit to ledger
    def add_deposit(self, amount, description):
        self.ledger = self.ledger.append({
            'Amount': round(amount, 2),
            'Balance': (self.ledger['Amount'].sum() + round(amount, 2)),
            'Description': description,
            'Category': 'Deposit',
        }, ignore_index=True)

