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
        self.inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }

    def add_new_order(self, customer, order, day):
        orders_options = self.get_available_dishes()

        for ingredient in self.INGREDIENTS[order]:
            self.inventory[ingredient] -= 1

        if order in orders_options:
            return self.orders.append([customer, order, day])

        return False

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

    def get_available_dishes(self):
        avaliable_dishes = set()

        """
        com consulta na solução do colega Matteus Fernandes,
        para entender onde estava meu erro:
        https://github.com/tryber/sd-013-c-restaurant-orders/pull/111
        """
        for dish in self.INGREDIENTS:
            has_ingredients = True

            for ingredient in self.INGREDIENTS[dish]:
                if self.inventory[ingredient] < 1:
                    has_ingredients = False
                if has_ingredients:
                    avaliable_dishes.add(dish)

        return avaliable_dishes
