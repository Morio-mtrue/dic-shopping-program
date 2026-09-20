# dic-shopping-program

Python object-oriented programming series assignment - Shopping program.

Completed from the `cdp_web_python_oop_task` starter.

## What was added

### Ownable imported into every class that needs an owner

`ownable.py` provides `set_owner`. The three classes whose instances have an
owner now include it the same way `User` includes `item_manager`:

- `Cart` (owned by the customer)
- `Item` (owned by the seller, then by the buyer)
- `Wallet` (owned by the user it belongs to)

### `Cart#check_out()`

```python
def check_out(self):
    if self.owner.wallet.balance < self.total_amount():
        print("残高が不足しているため購入できません")
        return

    for item in self.items:
        self.owner.wallet.withdraw(item.price)
        item.owner.wallet.deposit(item.price)
        item.set_owner(self.owner)

    self.items = []
```

For every item in the cart the price is withdrawn from the cart owner's wallet
and deposited into the item owner's wallet, ownership moves to the cart owner,
and the cart is emptied afterwards. If the cart owner cannot afford the total,
nothing is bought and the cart is left as it is.

## Verified

Buying 2 x 2.5インチSSD at 13,370 yen with a 200,000 yen balance:

| | Before | After |
| --- | --- | --- |
| Customer wallet | 200,000 | 173,260 |
| Seller wallet | 0 | 26,740 |
| Customer owns | nothing | 2 x 2.5インチSSD |
| Seller stock of that item | 10 | 8 |
| Cart | 2 items, 26,740 yen | empty, 0 yen |

## Run

```
pip install tabulate
cd lib/shopping_app
python3 shopping_app.py
```
