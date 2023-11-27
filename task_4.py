class AvgGrade:
    def avg_grade(self):
        all_grades = []
        for course, grades in self.grades.items():
            all_grades += grades
        return round((sum(all_grades) / len(all_grades)), 1)

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()


class Student(AvgGrade):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avg_grade()}\n' \
               f'Курсы в процессе изучения: ' \
               f'{", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(AvgGrade, Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.avg_grade()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


def avg_grade_homework(students, course):
    all_grades = []
    for student in students:
        if course in student.courses_in_progress \
                and student.grades.get(course):
            all_grades += student.grades[course]
    avg_grade_hw = round((sum(all_grades)/len(all_grades)), 1)

    return f'Cредняя оценка за домашние задания по {course}: {avg_grade_hw}'


def avg_grade_lecture(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached \
                and lecturer.grades.get(course):
            all_grades += lecturer.grades[course]
    avg_grade_lec = round((sum(all_grades)/len(all_grades)), 1)

    return f'Cредняя оценка за лекции по {course}: {avg_grade_lec}'


petr_petrov = Student('Petr', 'Petrov', 'male')
petr_petrov.courses_in_progress += ['Python', 'Git']
petr_petrov.add_courses('Computer_literacy')

ivan_ivanov = Student('Ivan', 'Ivanov', 'male')
ivan_ivanov.courses_in_progress += ['Python', 'JS', 'Git']
ivan_ivanov.add_courses('DB')
ivan_ivanov.add_courses('Computer_literacy')

mariya_krasnova = Mentor('Mariya', 'Krasnova')
mariya_krasnova.courses_attached += [
    'Python', 'JS', 'DB', 'Computer_literacy', 'Git'
]

aleksandr_nosov = Mentor('Aleksandr', 'Nosov')
aleksandr_nosov.courses_attached += ['Computer_literacy', 'Git']

oleg_bulygin = Lecturer('Oleg', 'Bulygin')
oleg_bulygin.courses_attached += ['Python', 'OOP', 'JS']

alena_batickaya = Lecturer('Alena', 'Batickaya')
alena_batickaya.courses_attached += ['Git']

aleksandr_bardin = Reviewer('Aleksandr', 'Bardin')
aleksandr_bardin.courses_attached += ['Python', 'OOP']

maksim_leskov = Reviewer('Maksim', 'Leskov')
maksim_leskov.courses_attached += ['Git', 'JS']

petr_petrov.rate_hw(oleg_bulygin, 'Python', 10)
petr_petrov.rate_hw(oleg_bulygin, 'Python', 10)
petr_petrov.rate_hw(oleg_bulygin, 'Python', 10)

petr_petrov.rate_hw(alena_batickaya, 'Git', 10)
petr_petrov.rate_hw(alena_batickaya, 'Git', 9)
petr_petrov.rate_hw(alena_batickaya, 'Git', 10)
comparison_lec = alena_batickaya.avg_grade() > oleg_bulygin.avg_grade()
print(comparison_lec)

aleksandr_bardin.rate_hw(petr_petrov, 'Python', 9)
aleksandr_bardin.rate_hw(petr_petrov, 'Python', 9)
aleksandr_bardin.rate_hw(petr_petrov, 'Python', 8)

aleksandr_bardin.rate_hw(ivan_ivanov, 'Python', 9)
aleksandr_bardin.rate_hw(ivan_ivanov, 'Python', 10)
aleksandr_bardin.rate_hw(ivan_ivanov, 'Python', 10)

maksim_leskov.rate_hw(ivan_ivanov, 'Git', 9)
maksim_leskov.rate_hw(ivan_ivanov, 'Git', 8)
maksim_leskov.rate_hw(ivan_ivanov, 'Git', 10)
comparison_stud = ivan_ivanov.avg_grade() > petr_petrov.avg_grade()
print(comparison_stud)

print(ivan_ivanov)
print(petr_petrov)
print(oleg_bulygin)
print(alena_batickaya)
print(aleksandr_bardin)
print(maksim_leskov)

print(avg_grade_homework(
    students=[petr_petrov, ivan_ivanov],
    course='Python'))
print(avg_grade_homework(
    students=[petr_petrov, ivan_ivanov],
    course='Git'))
print(avg_grade_lecture(
    lecturers=[oleg_bulygin, alena_batickaya],
    course='Git'))
print(avg_grade_lecture(
    lecturers=[oleg_bulygin, alena_batickaya],
    course='Python'))
