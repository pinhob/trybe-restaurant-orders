import csv
from typing import Counter


def get_requested_hamburguers_number(orders):
    most_requested_food = Counter(orders).most_common()

    for order in most_requested_food:
        if "hamburguer" in order[0]:
            hambuguers_request_number = order[1]
            return hambuguers_request_number

    return False


def get_maria_most_requested_food(orders):
    most_requested_food = Counter(orders).most_common()[0][0]
    return most_requested_food


def get_joao_unrequested_food_and_unvisited_days(options, orders):
    # adaptado de: https://stackoverflow.com/a/40185809/18637712
    return set(options) ^ set(orders)


def get_data(orders):
    foods_options = set()
    open_days = set()

    clients_orders = {}
    clients_frequency_days = {}

    for order in orders:
        foods_options.add(order["pedido"])
        open_days.add(order["dia"])

        if (
            order["cliente"] in clients_orders
            and order["cliente"] in clients_frequency_days
        ):
            clients_orders[order["cliente"]].append(order["pedido"])
            clients_frequency_days[order["cliente"]].append(order["dia"])
        else:
            clients_orders[order["cliente"]] = [order["pedido"]]
            clients_frequency_days[order["cliente"]] = [order["dia"]]

    maria_most_requested_orders = get_maria_most_requested_food(
        clients_orders["maria"]
    )

    arnaldo_requested_times = get_requested_hamburguers_number(
        clients_orders["arnaldo"]
    )

    joao_unrequested_foods = get_joao_unrequested_food_and_unvisited_days(
        foods_options, clients_orders["joao"]
    )

    joao_unvisited_days = get_joao_unrequested_food_and_unvisited_days(
        open_days, clients_frequency_days["joao"]
    )

    lines = [
        maria_most_requested_orders,
        arnaldo_requested_times,
        joao_unrequested_foods,
        joao_unvisited_days,
    ]

    return lines


# req. 1
def analyze_log(path_to_file):
    try:
        field_names = ["cliente", "pedido", "dia"]
        lines_to_write = []

        with open(path_to_file) as file:
            orders = csv.DictReader(file, fieldnames=field_names)
            lines_to_write = get_data(orders)

        with open("data/mkt_campaign.txt", "+w") as file:
            """
            com base:
            https://www.pythontutorial.net/python-basics/python-write-text-file/
            """
            for line in lines_to_write:
                file.write(str(line))
                file.write("\n")

    except FileNotFoundError:
        if path_to_file.endswith(".csv"):
            raise FileNotFoundError(f"Arquivo inexistente:' {path_to_file}'")
        else:
            raise FileNotFoundError(f"Extensão inválida:' {path_to_file}'")


if __name__ == "__main__":
    print(analyze_log("data/orders_1.csv"))
