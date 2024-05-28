class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.previous_transactions = []  
        
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity) 
        self.previous_transactions.append({"title": title, "price": price, "quantity": quantity})  # Record the transaction
        return self.items
        
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
            
    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        else:
            last_transaction = self.previous_transactions.pop()
            self.total -= last_transaction["price"] * last_transaction["quantity"]
            self.items = [item for item in self.items if item != last_transaction["title"]]
            return f"Voided {last_transaction['quantity']} {last_transaction['title']}(s) for ${last_transaction['price'] * last_transaction['quantity']}"