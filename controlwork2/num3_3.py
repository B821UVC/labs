import random
'''В соревнованиях участвуют три команды по 6 человек. Резуль- таты соревнований представлены в виде мест участников каждой ко- манды (1 - 18).
 Определить команду-победителя, вычислив количество баллов, набранное каждой командой. Участнику, занявшему 1-е место, начисляется 5 баллов, 2-е 4, 3-е 3, 4-е-2, 5-е 1, осталь- - 0 баллов.
При равенстве баллов победителем считается коман- да, за которую выступает участник, занявший 1-е место.'''
class Team:
    __lastId = 0
    def __init__(self, name="Default", list_players=[]):
        self.name = name
        self.members = list_players
        self.id = Team.__lastId
        Team.__lastId += 1
    def get_total_score(self):
        total = 0
        is_member_first = False
        for player in self.members:
            total += player.score
            if player.is_first:
                is_member_first = True
        return total, is_member_first

class Player:
    __lastId = 0
    instances = []
    def __init__(self, name="Default", score=0, team_id=0, is_first=False):
        self.name = name
        self.score = score
        self.id = Player.__lastId
        Player.__lastId += 1
        self.team_id = team_id
        self.is_first = is_first
        Player.instances.append(self)

    @classmethod
    def add_points_by_id(cls, id, points):
        for p in cls.instances:
            if p.id == id:
                p.score += points
                if points==5:
                    p.is_first = True


#create 3 teams 6 players each 

team1 = Team("Team 1", [Player("Player 1", 0, 0), Player("Player 2", 0, 0), Player("Player 3", 0, 0), Player("Player 4", 0, 0), Player("Player 5", 0, 0), Player("Player 6", 0, 0)])
team2 = Team("Team 2", [Player("Player 21", 0, 1), Player("Player 22", 0, 1), Player("Player 23", 0, 1), Player("Player 24", 0, 1), Player("Player 25", 0, 1), Player("Player 26", 0, 1)])
team3 = Team("Team 3", [Player("Player 31", 0, 2), Player("Player 32", 0, 2), Player("Player 33", 0, 2), Player("Player 34", 0, 2), Player("Player 35", 0, 2), Player("Player 36", 0, 2)])

#присвоим случайным игрокам очки баллы даются за 5 мест всего id 18: 0-17
lst_winners = []

while len(lst_winners)<5:
    num = random.randint(0,17)
    if num not in lst_winners:
        lst_winners.append(num)
print("Список id победителей:", lst_winners)
points =5
for i in lst_winners:
    Player.add_points_by_id(i, points)
    points -= 1

if (team1.get_total_score()[0] > team2.get_total_score()[0]) and (team1.get_total_score()[0] > team3.get_total_score()[0]):
    print(team1.name, team1.get_total_score()[0])
elif (team2.get_total_score()[0] > team1.get_total_score()[0]) and (team2.get_total_score()[0] > team3.get_total_score()[0]):
    print(team2.name, team2.get_total_score()[0])
if team1.get_total_score()[0] == team2.get_total_score()[0] and team1.get_total_score()[0]>team3.get_total_score()[0]:
    if team1.get_total_score()[1]:
        print(team1.name, team1.get_total_score()[0])
    else:
        print(team2.name, team2.get_total_score()[0])
if team1.get_total_score()[0] == team3.get_total_score()[0] and team1.get_total_score()[0]>team2.get_total_score()[0]:
    if team1.get_total_score()[1]:
        print(team1.name,  team1.get_total_score()[0])
    else:
        print(team3.name, team3.get_total_score()[0])
if team2.get_total_score()[0] == team3.get_total_score()[0] and team2.get_total_score()[0]>team1.get_total_score()[0]:
    if team2.get_total_score()[1]:
        print(team2.name, team2.get_total_score()[0])
    else:
        print(team3.name, team2.get_total_score()[0])
