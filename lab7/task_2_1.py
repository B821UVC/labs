'''Студенты одной группы в сессию сдают четыре экзамена. Составить список студентов, средний балл которых
по всем экзаменам не менее «4».
Результаты вывести в виде таблицы с заголовком в порядке убывания среднего балла.'''


class Student:
    def __init__(self, name, exam1, exam2, exam3, exam4):
        self.name = name
        self.exam1 = exam1
        self.exam2 = exam2
        self.exam3 = exam3
        self.exam4 = exam4

    def get_average(self):
        return (self.exam1 + self.exam2 + self.exam3 + self.exam4) / 4
    

class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_studenst_higher_4(self):
        res = []
        for student in self.students:
            if student.get_average() >= 4:
                res.append([student.name, student.get_average()])
        return res
    


group = Group("Group 1")
group.add_student(Student("Ivan", 5, 5, 5, 5))  
group.add_student(Student("Aleksey", 5, 4, 5, 4))                                                          
group.add_student(Student("Petr", 4, 4, 4, 4))                                                             
group.add_student(Student("Oleg", 3, 3, 3, 3))                                                             
group.add_student(Student("Vladimir", 2, 2, 2, 2))                                                         
group.add_student(Student("Viktor", 1, 1, 3, 3))
group.add_student(Student("Mikhail", 4, 2, 3, 3))


for student in group.get_studenst_higher_4():
    print(f"{student[0]}: {student[1]}")
