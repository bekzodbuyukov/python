from math import pi


class Cone:
    def __init__(self, radius: int, height: int,
                 density: int, weight: bool, volume: bool) -> None:
        self.radius = radius
        self.height = height
        self.density = density
        self.calculate_weight_option = weight
        self.calculate_volume_option = volume
        self.base_area = pi * pow(self.radius, 2)
        self.weight = 0
        self.volume = 0

    def calculate_volume(self):
        if self.calculate_volume_option:
            self.volume = (1 / 3) * self.base_area * self.height
        else:
            return ""

    def calculate_weight(self):
        if self.calculate_weight_option:
            pass
