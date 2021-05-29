import string
from faker import Faker

from student import Student
from teacher import Teacher


def start_process():
    students = []
    teacher = Teacher("John", "Doe", 27, "Math")

    fake = Faker()
    for _ in range(5):
        first_name, last_name = fake.name().split()[0:2]
        age = fake.numerify("##")
        group = fake.lexify("????", string.ascii_letters)

        student = Student(first_name, last_name, age, group)
        student.__setattr__("teacher", teacher)
        students.append(student)

        print(student)

    teacher.__setattr__("students", students)
    print(teacher)


if __name__ == "__main__":
    start_process()
