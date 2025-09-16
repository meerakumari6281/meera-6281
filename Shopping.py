class Sc:
    def __init__(self):
        self.items = []
    def add_item(self,item_name, qty):
        item = (item_name, qty)
        self.items.append(item)
        print(f"Added {qty} {item_name} to the cart.")
    def remove_item(self, item_name):
        for i,(name, qty) in enumerate(self.items):
            if name == item_name:
                del self.items[i]
                print(f"Removed {item_name} from the cart")
                return
        print(f"{item_name} not found in the cart")
    def calculate_total(self):
        total =0
        for item in self.items:
            total += item[1]
        return total
    def show_cart(self):
        if not self.items:
            print("Cart is empty")
        else:
            print("Items in the cart:")
            for name, qty in self.items:
                print(f"{name}: {qty}")
            print(f"Total: {self.calculate_total()}")

cart = Sc()
cart.add_item("Papaya", 100)
cart.add_item("Guva", 200)
cart.add_item("Orange", 150)

cart.show_cart()
cart.remove_item("Guva")
cart.show_cart()

print(f"Final Total: {cart.calculate_total()}")
