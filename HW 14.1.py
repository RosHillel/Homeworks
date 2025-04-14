class TooManyStudentsError(Exception):
    pass

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, № залікової: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudentsError("У групі може бути не більше 10 студентів.")
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group {self.number}:\n{all_students}"

group = Group('PD1')
for i in range(10):
    st = Student('Male', 20+i, f'Імя{i}', f'Прізвище{i}', f'RB{i}')
    group.add_student(st)

print(group)

try:
    extra_student = Student('Female', 22, 'Олена', 'Додаткова', 'RB11')
    group.add_student(extra_student)
except TooManyStudentsError as e:
    print(e)

print(group)
