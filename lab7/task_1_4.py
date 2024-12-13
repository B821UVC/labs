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

lst_of_participants = []
for i in range(4):
    print("Введите в порядке: имя, возраст, попытка 1, попытка 2. Каждое значение с новой строки")
    name = input()
    age = int(input())
    attempt1 = int(input())
    attempt2 = int(input())
    lst_of_participants.append(competiton_participant(name, age, attempt1, attempt2))
lst_of_participants.sort(key = lambda x: x.get_best_attempt(), reverse = True)
for i in range(4):
    print(i+1, lst_of_participants[i].name, lst_of_participants[i].get_best_attempt())