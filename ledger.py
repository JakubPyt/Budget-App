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

    # Func check funds on account and if funds >= withdraw amount, it adds this withdraw
    def add_withdraw(self, amount, description, category):
        if self.ledger['Amount'].sum() >= amount:
            self.ledger = self.ledger.append({
                'Amount': round(-amount, 2),
                'Balance': (self.ledger['Amount'].sum() - round(amount, 2)),
                'Description': description,
                'Category': category
            }, ignore_index=True)
            return True
        else:
            return "You don't have enough funds in your account"

    # Func return ledger or string(if ledger is empty)
    def get_ledger(self, one_column=''):
        if one_column == '':
            if len(self.ledger) == 0:
                return "The ledger is empty, add first deposits and withdraws"
            else:
                return self.ledger
        elif one_column == 'index':
            return self.ledger.index
        else:
            return self.ledger[one_column]

    def get_expenses_by_category(self):
        category_amount_df = self.ledger[['Category', 'Amount']].where(self.ledger['Category'] != 'Deposit')
        expenses_by_category = category_amount_df.groupby('Category').sum().abs()
        return expenses_by_category
