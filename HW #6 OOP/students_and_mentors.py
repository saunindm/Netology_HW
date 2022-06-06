class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _get_average_grade(self):
        all_grades_list = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades_list.append(grade)
        average_grade = sum(all_grades_list) / len(all_grades_list)
        return average_grade

    def _get_student_info(self):
        return f"Name: {self.name} \n" \
               f"Surname: {self.surname} \n" \
               f"Average grade for homework: {self._get_average_grade()} \n" \
               f"Courses in progress: {', '.join(self.courses_in_progress)} \n" \
               f"Finished courses: {','.join(self.finished_courses)}"

    def __str__(self):
        res = f'{self._get_student_info()}'
        return res

    def __le__(self, other):
        return self._get_average_grade() <= other._get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    pass

    def _get_average_grade(self):
        all_grades_list = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades_list.append(grade)
        average_grade = sum(all_grades_list) / len(all_grades_list)
        return average_grade

    def _get_lecturer_info(self):
        return f'Name: {self.name} \n' \
               f'Surname: {self.surname} \n' \
               f'Average grade for lectures: {self._get_average_grade()}'

    def __str__(self):
        res = f'{self._get_lecturer_info()}'
        return res

    def __le__(self, other):
        return self._get_average_grade() <= other._get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Name: {self.name}\nSurname: {self.surname}'
        return res


def get_avg_hw_grade(students, specific_course):
    all_grades = []
    for names, courses in students.items():
        all_grades.extend(courses[specific_course])
    average_grade = sum(all_grades) / len(all_grades)
    return average_grade


def get_avg_lctr_grade(lecturers, specific_course):
    all_grades = []
    for names, courses in lecturers.items():
        all_grades.extend(courses[specific_course])
    average_grade = sum(all_grades) / len(all_grades)
    return average_grade


harry = Student('Harry', 'Potter', 'Male')
harry.courses_in_progress += ['Defence Against the Dark Arts', 'Care of Magical Creatures', 'Charms']
harry.finished_courses += ['Quidditch']
hermione = Student('Hermione', 'Granger', 'Female')
hermione.courses_in_progress += ['Defence Against the Dark Arts', 'Care of Magical Creatures', 'Charms']
hermione.finished_courses += ['Quidditch']

albus = Reviewer('Albus', 'Dumbledore')
albus.courses_attached += ['Defence Against the Dark Arts', 'Care of Magical Creatures', 'Charms']
minerva = Reviewer('Minerva', 'Mcgonagall')
minerva.courses_attached += ['Defence Against the Dark Arts', 'Care of Magical Creatures', 'Charms']

severus = Lecturer('Severus', 'Snape')
severus.courses_attached += ['Defence Against the Dark Arts', 'Charms']
hagrid = Lecturer('Rubeus', 'Hagrid')
hagrid.courses_attached += ['Care of Magical Creatures', 'Charms']

# вызов метода выставления оценок за лекции
albus.rate_hw(harry, 'Defence Against the Dark Arts', 9)
albus.rate_hw(harry, 'Care of Magical Creatures', 7)
albus.rate_hw(harry, 'Charms', 8)
minerva.rate_hw(hermione, 'Defence Against the Dark Arts', 9)
minerva.rate_hw(hermione, 'Care of Magical Creatures', 10)
minerva.rate_hw(hermione, 'Charms', 9)

# вызов метода выставления оценок за лекции
harry.rate_lecturer(severus, 'Defence Against the Dark Arts', 2)
harry.rate_lecturer(severus, 'Charms', 3)
harry.rate_lecturer(hagrid, 'Care of Magical Creatures', 10)
harry.rate_lecturer(hagrid, 'Charms', 7)
hermione.rate_lecturer(severus, 'Defence Against the Dark Arts', 5)
hermione.rate_lecturer(severus, 'Charms', 10)
hermione.rate_lecturer(hagrid, 'Care of Magical Creatures', 10)
hermione.rate_lecturer(hagrid, 'Charms', 10)

# проверки перегрузки методов __str__
# print(harry)
# print(hermione)
# print()
# print(severus)
# print(hagrid)
# print()
# print(albus)
# print(minerva)
# print()

# проверки методов выставления оценок
print(severus.grades)
print(hagrid.grades)
print()
print(harry.grades)
print(hermione.grades)
print()

# проверка перегрузки методов __le__
# print(harry <= hermione)
# print(hagrid <= severus)
# print()

# словари студентов и лекторов
# students_list = {harry: harry.grades, hermione: hermione.grades}
# lecturers_list = {severus: severus.grades, hagrid: hagrid.grades}

# проверка реализаций функций подсчета средних оценок
# print(get_avg_hw_grade(students_list, 'Care of Magical Creatures'))
# print(get_avg_lctr_grade(lecturers_list, 'Charms'))