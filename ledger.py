import pandas as pd


class Ledger:
    def __init__(self):
        # Create empty ledger to storage information about all operations
        # Ledger is dataframe object
        self.ledger = pd.DataFrame(
            columns=[
                'Amount',  # The amount of the payment
                'Balance',  # Account balance after the operation
                'Description',  # Description of the operation
                'Category'  # "Deposit" for each deposit and custom for each withdrawal
            ]
        )

    def add_deposit(self, amount, description):
        """
        Function add deposit to ledger.
        :param amount: int, float
        :param description: str
        :return: None
        """
        self.ledger = self.ledger.append({
            # Param round to 2
            'Amount': round(amount, 2),
            # Calculated automatically: current balance + above amount
            'Balance': (self.ledger['Amount'].sum() + round(amount, 2)),
            # Param from the user
            'Description': description,
            # For each deposit the same category
            'Category': 'Deposit',
        }, ignore_index=True)

    def add_withdrawal(self, amount, description, category):
        """
        Function check funds on account and if funds >= withdrawal amount,
        it adds this withdrawal and returns True. Else only returns false.
        :param amount: int, float
        :param description: str
        :param category: str
        """
        # Check if you have funds
        if self.ledger['Amount'].sum() >= amount:
            self.ledger = self.ledger.append({
                # Param round to 2 and add with -
                'Amount': round(-amount, 2),
                # Calculated automatically: current balance - above amount
                'Balance': (self.ledger['Amount'].sum() - round(amount, 2)),
                # Param from the user
                'Description': description,
                # Param from the user
                'Category': category
            }, ignore_index=True)
            return True
        else:
            # If you not have enough funds
            return False


    def get_ledger(self, one_column=''):
        """
        Function return:
         - string if ledger is empty
         - entire ledger(default)
         - one column from ledger(given in the parameter)
         - index of ledger(if one_column='index')
        :param one_column: column name, str
        """
        if len(self.ledger) == 0:
            return "The ledger is empty, add first deposits and withdrawals"
        elif one_column == '':
            return self.ledger
        elif one_column == 'index':
            return self.ledger.index
        else:
            return self.ledger[one_column]

    def get_expenses_by_category(self):
        """
        Function calculate expenses in each category(without "Deposit").
        :return: DataFrame with category as index and column with sum of amounts in this category.
        """
        # Take only columns "category" and "amount"
        # Where "Category" is not 'Deposit'
        category_amount_df = self.ledger[['Category', 'Amount']]\
            .where(self.ledger['Category'] != 'Deposit')
        # Sum absolute values in each category
        expenses_by_category = category_amount_df\
            .groupby('Category').sum().abs()
        return expenses_by_category
