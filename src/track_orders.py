from typing import Counter


class TrackOrders:
    def __init__(self) -> None:
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])
        print(self.orders)

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = []

        for order in self.orders:
            if order[0] == customer:
                customer_orders.append(order[1])

        most_requested_food = Counter(customer_orders).most_common()[0][0]
        return most_requested_food

    def get_never_ordered_per_customer(self, customer):
        food_options = set()
        customer_orders = set()

        for order in self.orders:
            food_options.add(order[1])

            if order[0] == customer:
                customer_orders.add(order[1])

        return food_options ^ customer_orders

    def get_days_never_visited_per_customer(self, customer):
        open_days = set()
        visited_days_per_customer = set()

        for order in self.orders:
            open_days.add(order[2])

            if order[0] == customer:
                visited_days_per_customer.add(order[2])

        return open_days ^ visited_days_per_customer

    def get_busiest_day(self):
        visited_days = []

        for order in self.orders:
            visited_days.append(order[2])

        most_visited_day = Counter(visited_days).most_common()[0][0]
        return most_visited_day

    def get_least_busy_day(self):
        visited_days = []

        for order in self.orders:
            visited_days.append(order[2])

        most_visited_day = Counter(visited_days).most_common()[-1][0]
        return most_visited_day
