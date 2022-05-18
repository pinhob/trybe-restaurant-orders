class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.orders = []

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_quantities_to_buy(self):
        order_ingredients = []

        for order in self.orders:
            order_ingredients.extend(self.INGREDIENTS[order[1]])

        total_ingredients = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

        for ingredient in order_ingredients:
            total_ingredients[ingredient] += 1

        return total_ingredients
