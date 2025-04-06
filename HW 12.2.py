class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


    def __eq__(self, other):
        if isinstance(other, Item):
            return (self.name, self.price, self.description, self.dimensions) == (other.name, other.price, other.description, other.dimensions)
        return False

    def __hash__(self):
        return hash((self.name, self.price, self.description, self.dimensions))


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        items_str = "\n".join(f"{item.name}: {cnt} pcs." for item, cnt in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}"



lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert cart.get_total() == 60, "Всього 60"  # 4*5 + 20*2 = 20 + 40 = 60

cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40, 'Повинно залишатися 40!'  # 4*5 + 10*2 = 20 + 20 = 40

print("Ok")
