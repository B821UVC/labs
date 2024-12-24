'''5. Соревнования по прыжкам на лыжах со 120-метрового трам- плина оценивают 5 судей.
Каждый судья выставляет оценку за стиль прыжка по 20-балльной шкале. Меньшая и большая оценки отбрасываются, остальные суммируются.
К этой сумме прибавляются очки за дальность прыжка: 120 м - 60 очков, за каждый метр превышения добавляются по 2 очка, при меньшей дальности отнимаются 2 очка за каждый метр.
Получить итоговую таблицу соревнований, содержащую фамилию и итоговый результат для каждого участника в поряд
ке занятых мест.'''
def get_max_min(points):
    max_elem = points[0]
    min_elem = points[0]
    for i in range(len(points)):
        if points[i]>max_elem:
            max_elem = points[i]
        if points[i]<min_elem:
            min_elem = points[i]
    return max_elem, min_elem

def get_sum(points):
    sum = 0
    for i in range(len(points)):
        sum+=points[i]
    return sum


class Sportsman:
    def __init__(self, last_name,long:int, points:list):
        self.name = last_name
        self.long = long
        self.points = points
    def get_points(self):
        long_points = 60 + (self.long-120)*2
        judge_points = get_sum(self.points) - get_max_min(self.points)[0]-get_max_min(self.points)[1]
        return long_points + judge_points

class Competition:
    def __init__(self, list_of_sportsman:list):
        self.list_of_sportsman = list_of_sportsman

    def get_winners(self):
        return sorted(self.list_of_sportsman, key = lambda x: x.get_points(), reverse = True)
    
#создадим участицов
sportsman1 = Sportsman("Иванов", 170, [12, 13, 14, 15, 16,])
sportsman2 = Sportsman("Петров", 130, [10, 11, 12, 13, 9,])
sportsman3 = Sportsman("Сидоров", 110, [8, 9, 10, 11, 12,])
sportsman4 = Sportsman("Кузнецов", 160, [6, 7, 8, 9, 15,])
sportsman5 = Sportsman("Смирнов", 120, [2, 5, 11, 14, 8,])

list_of_sportsman = [sportsman1, sportsman2, sportsman3, sportsman4, sportsman5]
competition = Competition(list_of_sportsman)

winners = competition.get_winners()
for i in range(len(winners)):
    print(winners[i].name, winners[i].get_points())
