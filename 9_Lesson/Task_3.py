class Worker:
    def __init__(self, wage, bonus, name, surname, position):
        self.__income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position

class Position(Worker):
    def __init__(self, wage, bonus, name, surname, position):
        super().__init__(wage, bonus, name, surname, position)
#
    def get_full_name(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nДолжность: {self.position}'
#
    def get_total_income(self):
        return f'Доход с учётном премии {p._Worker__income}'



p = Position(50000, 1000, 'Eugen', 'Varlamov', 'IT-specialist')
print(p.get_full_name())
print(p.get_total_income())
