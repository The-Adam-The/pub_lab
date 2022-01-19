class Pub:
    def __init__(self, name, till, drink_list):
        self.name = name
        self.till = till
        self.drink_list = drink_list
        self.alchohol_limit_ = 15


    def increase_till(self, amount):
        self.till += amount

    def customer_legal_age(self, customer_age):
        # if customer_age >= 18:
        #     return True
        # return False
        return True if customer_age >= 18 else False

    def decline_service_too_drunk(self, customer_drunkenness, pub_alcohol_limit):
        return True if customer_drunkenness >= pub_alcohol_limit else False

    def purchase_drink(self, drink, customer):
        if self.customer_legal_age(customer.age):
            self.increase_till(drink.price)
            customer.lower_wallet_balance(drink.price)
            customer.increase_drunkenness(drink.alcohol_level)


    

