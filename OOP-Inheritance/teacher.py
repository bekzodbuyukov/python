from person import Person


class Teacher(Person):
    def __init__(self, first_name: str, last_name: str,
                 age: int, subject: str) -> None:
        self.subject = subject
        self.students = []
        super().__init__(first_name, last_name, age)

    def extend_students_list(self, new_students: list):
        self.students.extend(new_students)

    def __repr__(self) -> str:
        return f"\nTeacher: {self.first_name} {self.last_name}" \
               f"\nAge: {self.age} y.o." \
               f"\nSubject: {self.subject}" \
               + "\nStudents: {}".format(self.students)
