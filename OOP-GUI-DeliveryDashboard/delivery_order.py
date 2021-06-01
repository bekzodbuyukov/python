import re


class DeliveryOrder:
    """ Class for managing Delivery Orders """
    def __init__(self, distance: int, name: str, date: str, car_number: str) -> None:
        self.distance = distance
        self.product_name = name
        self.delivery_date = date
        self.car_number = car_number

    def is_delivery_date_similar(self, comparing_date: str) -> bool:
        return bool(
            re.fullmatch(pattern=comparing_date, string=self.delivery_date)
        )

    def __repr__(self) -> str:
        return f"Delivery Order details:" \
               f"\nProduct name: {self.product_name}" \
               f"\nDistance: {self.distance} km." \
               f"\nDate: {self.delivery_date}" \
               f"\nDelivery car: {self.car_number}"
