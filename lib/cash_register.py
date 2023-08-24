#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, item, price, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        
        transaction_total = price * quantity
        self.total += transaction_total
        self.items.extend([item] * quantity)
        
        transaction = {"item": item, "quantity": quantity, "price": price, "total": transaction_total}
        self.transactions.append(transaction)

    def apply_discount(self):
        if self.discount:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the {self.discount}% discount, the new total is ${self.total:.2f}.")
        else:
            print("No discount is applicable.")

    def void_last_transaction(self):
        if not self.transactions:
            return "No transactions to void."
        
        last_transaction = self.transactions.pop()
        self.total -= last_transaction["total"]
        self.items = self.items[:-last_transaction["quantity"]]

        return f"Transaction for {last_transaction['item']} ({last_transaction['quantity']} item(s)) has been voided."

# Example usage
register = CashRegister(discount=10)

register.add_item("Apple", 0.75, quantity=4)
register.add_item("Banana", 0.50)
register.add_item("Orange", 1.25, quantity=2)

print("Items in the cart:", register.items)
print("Total before discount:", register.total)

register.apply_discount()

print("Items in the cart:", register.items)
print("Total after discount:", register.total)

print(register.void_last_transaction())
print("Items in the cart:", register.items)
print("Total after voiding:", register.total)

