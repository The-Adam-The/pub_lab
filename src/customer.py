class Customer:
    
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def lower_wallet_balance(self, amount):
        self.wallet -= amount