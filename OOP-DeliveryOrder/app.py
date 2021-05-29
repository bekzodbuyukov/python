import json
import sys

from delivery_order import DeliveryOrder


def start_process(user_input: str) -> None:
    try:
        file = open(file="mock_data.json", mode="r")
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()
    except OSError as error:
        print(f"Error: Error {error.errno} {error.strerror}")
        sys.exit()
    else:
        contents = json.loads(file.read())
        file.close()

    orders = []
    for content in contents["orders"]:
        orders.append(DeliveryOrder(
            content["distance"],
            content["product_name"],
            content["delivery_date"],
            content["car_number"]
        ))

    for order in orders:
        if order.is_delivery_date_similar(user_input):
            print(order, end="\n\n")


if __name__ == "__main__":
    user_new_input = "07.07.2021"
    start_process(user_new_input)
