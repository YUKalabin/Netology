class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self.avg_grade()}\n'
        f'Курсы в процессе изучения: {self.courses_in_progress}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def avg_grade(self):
        sum_grade = 0
        count_grade = 0
        for value in self.grades.values():
            print(value)
            sum_grade += sum(value)
            count_grade += len(value)
        if count_grade > 0:
            return (sum_grade / count_grade)
        else:
            return 0

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за лекции: {self.avg_grade()}\n')

    def avg_grade(self):
        sum_grade = 0
        count_grade = 0
        for value in self.grades.values():
            print(value)
            sum_grade += sum(value)
            count_grade += len(value)
        if count_grade > 0:
            return (sum_grade / count_grade)
        else:
            return 0



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
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n')


def avg_grade_stud_all(students, course):
    sum_grades = 0
    count_grades = 0
    for stud in students:
        if course in stud.grades:
            sum_grades += sum(stud.grades[course])
            count_grades += len(stud.grades[course])
    if count_grades > 0:
        return (sum_grades / count_grades)
    else:
        return None





 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['HTML']

worst_student = Student('Kolya', 'K', 'your_gender')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ['CSS']

best_lecturer = Lecturer('Roy', 'V')
best_lecturer.courses_attached += ['Python']

worst_lecturer = Lecturer('Viktor', 'P')
worst_lecturer.courses_attached += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

worst_reviewer = Reviewer('Some2', 'Buddy2')
worst_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_l(best_lecturer, 'Python', 8)
best_student.rate_l(best_lecturer, 'Python', 7)
best_student.rate_l(best_lecturer, 'Python', 9)

students = [best_student, worst_student]

print(avg_grade_stud_all(students, 'Python'))
 
print(best_student.grades)
print(best_lecturer.grades)
print(best_student)
print(best_lecturer)
print(cool_reviewer)