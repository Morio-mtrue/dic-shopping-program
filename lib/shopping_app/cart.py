class Cart:
    # Ownable gives the cart an owner (set_owner / self.owner).
    from ownable import set_owner
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        # Not enough money in the cart owner's wallet: buy nothing.
        if self.owner.wallet.balance < self.total_amount():
            print("残高が不足しているため購入できません")
            return

        for item in self.items:
            # The price is withdrawn from the cart owner's wallet and
            # deposited into the item owner's wallet.
            self.owner.wallet.withdraw(item.price)
            item.owner.wallet.deposit(item.price)
            # Ownership of the item moves to the cart owner.
            item.set_owner(self.owner)

        # The cart is emptied once every item has been paid for.
        self.items = []
