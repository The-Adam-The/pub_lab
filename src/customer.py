class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def lower_wallet_balance(self, amount):
        self.wallet -= amount