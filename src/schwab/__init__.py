__version__ = "0.0.1"

import click

from . import api, stream
from datetime import datetime, timedelta


def main():
    # get accounts numbers for linked accounts
    print(api.Accounts.accountNumbers().json())

    # get positions for linked accounts
    print(api.Accounts.getAllAccounts().json())

    # get specific account positions
    print(api.Accounts.getAccount(fields="positions").json())

    # get up to 3000 orders for all accounts for the past week
    print(api.Orders.getAllOrders(3000, datetime.now() - timedelta(days=7), datetime.now()).json())

    # get all transactions for an account
    print(api.Transactions.transactions(datetime.now() - timedelta(days=7), datetime.now(), "TRADE").json())


@click.command()
def demo():
    api.initialize()  # checks tokens & loads variables
    api.updateTokensAutomatic()  # starts thread to update tokens automatically
    main()

if __name__ == "__main__":
    demo()
