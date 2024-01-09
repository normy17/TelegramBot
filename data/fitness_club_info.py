class Coach:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


class Group:
    def __init__(self, name, desc, coaches, time):
        self.name = name
        self.desc = desc
        self.coaches = coaches
        self.time = time


coach1 = Coach("Тренер 1", "Крутой тренер")
coach2 = Coach("Тренер 2", "Очень крутой тренер")

group1 = Group("Плавание", "Описание плавания", coaches=[coach2], time=["17:00", "", "15:30", "", "", "12:00", ""])
group2 = Group("Йога", "Описание йоги", coaches=[coach1], time=["12:00", "15:00", "15:30", "13:00", "13:00", "", "10:00"])
group3 = Group("Большая группа", "Описание большой группы", coaches=[coach1, coach2], time=["12:00", "10:00", "", "19:00", "", "", "19:00"])

coaches = [coach1, coach2]
groups = [group1, group2, group3]