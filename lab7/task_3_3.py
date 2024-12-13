#https://stackoverflow.com/questions/53449804/python-find-instance-of-a-class-by-value
class Person:
    __personId = 0
    instances = []
    def __init__(self, first_name="Default", last_name="Default", score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.id = Person.__personId
        Person.__personId += 1
        Person.instances.append(self)
    def add_score(self, points):
        self.score += points
    @classmethod
    def search_by_name(cls, f_name="None", s_name="None"):
        for p in cls.instances:
            if p.first_name == f_name and p.last_name == s_name:
                return p
    @classmethod
    def search_by_id(cls, id):
        for p in cls.instances:
            if p.id == id:
                return p

    

class Team:
    __lastId = 1
    def __init__(self, name="Default", list_players=[]):
        self.name = name
        self.members = list_players
        self.id = Team.__lastId
        Team.__lastId += 1
    def get_total_score(self):
        total = 0
        for player in self.members:
            total += player.score
        return total
    

class Competition:
    def __init__(self, list_teams=[]):
        self.teams = list_teams
    def set_winners(self,list_of_winners):  #получает на вход список который может быть заполнен как id так и именем и фамилей
        for i in range(5):   #за пять мест присуждаются очки i==4 максимум
            points = 0
            if i==0:
                points = 5
            elif i==1:
                points = 4
            elif i==2:
                points = 3
            elif i==3:
                points = 2
            elif i==4:
                points = 1
            if(type(list_of_winners[i])) == int:
                print(list_of_winners[i])
                Person.search_by_id(list_of_winners[i]).add_score(points)
            else:
                first_name, last_name = list_of_winners[i].split()
                Person.search_by_name(first_name, last_name).add_score(points)

        self.teams.sort(key = lambda x: x.get_total_score(), reverse = True)
    def get_teams(self):
        return self.teams


#сначала создаем команды в которых по шесть человек
team1 = Team("team1", [Person("A","B"), Person("C","D"), Person("E","F"), Person("G","H"), Person("I","J"), Person("K","L")])
team2 = Team("team2", [Person("M","N"), Person("O","P"), Person("Q","R"), Person("S","T"), Person("U","V"), Person("W","X")])
team3 = Team("team3", [Person("Y","Z"), Person("AA","BB"), Person("CC","DD"), Person("EE","FF"), Person("GG","HH"), Person("II","JJ")])
#далее создаем конкурс
comp = Competition([team1, team2, team3])
#создаем список победителей
winners = ["AA BB", "CC DD", "EE FF", "GG HH", "II JJ"]
#присваиваем очки
comp.set_winners(winners)
#выводим результат
for i in comp.get_teams():
    print(i.name, i.get_total_score())


#тест №2
team4 = Team("team4", [Person("AKK","BKK"), Person("CKK","DKK"), Person("EKK","FKK"), Person("GKK","HKK"), Person("IKK","JKK"), Person("KLL","LLLL")])
team5 = Team("team5", [Person("Mhhh","Nhhhh"), Person("Ohh","Phh"), Person("Qhh","Rhh"), Person("Shh","Thh"), Person("Uhh","Vhh"), Person("Whh","Xhh")])
team6 = Team("team6", [Person("Yhh","Zhh"), Person("AAhh","BBhh"), Person("CChh","DDhhh"), Person("EEhh","FFhh"), Person("GGhhh","HHhh"), Person("IIhh","JJhhh")])
#далее создаем конкурс
comp2 = Competition([team4, team5, team6])
winners = ["AKK BKK", 20, "IIhh JJhhh", 29, "IKK JKK"]
comp2.set_winners(winners)
#выводим результат
for i in comp2.get_teams():
    print(i.name, i.get_total_score())