from person import Person


class Student(Person):
    def __init__(self, first_name: str, last_name: str,
                 age: int, group: str) -> None:
        self.group = group
        self.teacher = None
        super().__init__(first_name, last_name, age)

    def __repr__(self) -> str:
        return f"\nStudent: {self.first_name} {self.last_name}" \
               f"\nAge: {self.age} y.o." \
               f"\nGroup: {self.group}" \
               # f"\nTeacher: {self.teacher}"
