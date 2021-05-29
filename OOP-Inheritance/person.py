
class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.age} y.o."
