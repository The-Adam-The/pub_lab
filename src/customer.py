class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def lower_wallet_balance(self, amount):
        self.wallet -= amount

    def increase_drunkenness(self, alchohol_level):
        self.drunkenness += alchohol_level