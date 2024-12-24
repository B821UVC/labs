'''Результаты соревнований фигуристов по одному из видов многоборья представлены оценками 7 судей в баллах (от 0,0 до 6,0). По
результатам оценок судьи определяется место каждого участника у этого судьи. 
Места участников определяются далее по сумме мест, которые каждый участник занял у всех судей. 
Составить программу, определяющую по исходной таблице оценок фамилии и сумму мест участников в порядке занятых ими мест.'''
JUDGE_COUNT = 7
MAX_SCORE = 6.0
MIN_SCORE = 0.0
import random
class Figure_skater:
    def __init__(self, lastname:str, points: list, places=0):
        self.lastname = lastname
        self.points = points
        self.places = 0
    def get_points(self, judge_num):
        return self.points[judge_num]
    def set_places(self, place):
        self.places += place
    def get_sum_places(self):
        return self.places
    def get_name(self):
        return self.lastname
    def __str__(self):
        return f"{self.get_name()} : {self.get_sum_places()}"

class Tablesheet:
    def __init__(self, list_of_figures: list):
        self.list_of_figures = list_of_figures
    def get_figures(self):
        return self.list_of_figures
    def sort_table(self):
        lst_figures = self.list_of_figures
        for judge in range(JUDGE_COUNT):
            scores = []
            for participant in lst_figures:
                scores.append([participant.get_points(judge), participant])
            scores.sort(key = lambda x: x[0], reverse = True)
            for i in range(len(scores)):
                participant = scores[i][1]
                participant.set_places(i+1)
        lst_figures.sort(key = lambda x: x.get_sum_places())

lst_names = ["Antonov", "Tupolev", "Pelotonov", "Hamilton", "Kvyat"]
lst_figures = []
for i in range(5):
    points = [random.random()*6 for x in range(7)]
    lst_figures.append(Figure_skater(lst_names[i], points))
table = Tablesheet(lst_figures)
table.sort_table()
place = 1
for i in table.get_figures():
    print(place, i)
    place+=1
