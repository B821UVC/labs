class competiton_participant:
    def __init__(self, name, age, attempt1, attempt2):
        self.name = name
        self.age = age
        self.attempt1 = attempt1
        self.attempt2 = attempt2
    def get_best_attempt(self):
        if self.attempt1 > self.attempt2:
            return self.attempt1
        else:
            return self.attempt2

lst_of_participants = [competiton_participant("Igor", 22, 200, 180), competiton_participant("Winner", 25, 230, 168), competiton_participant("nikita", 18, 194, 178), competiton_participant("kolya", 20, 177, 188)]
lst_of_participants.sort(key = lambda x: x.get_best_attempt(), reverse = True)
for i in range(4):
    print(i+1, lst_of_participants[i].name, lst_of_participants[i].get_best_attempt())
