class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f'Машина {self.name} {self.color} сдвинулась с места')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')

    def police_activity(self):
        if self.is_police == True:
            print('Это полиция')
            if scar.speed > 150:
                print(f'\nВнимание База, превышение скорости более чем {scar.speed - 150} км/ч\n'
                      f'Ориентировачные данные машины:\n'
                      f'Марка машины: {scar.name}\n'
                      f'Цвет: {scar.color}\n'
                      f'Веду преследование!!!')
        else:
            print('Это не полиция')


class TownCar(Car):
    speed_limit = 60
    def __init__(self, speed, color, name, is_police=bool):
        super().__init__(speed, color, name, is_police=bool)

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Скорость: {self.speed} км/ч\n'
                  f'Превышение скорости на {self.speed - self.speed_limit} км/ч !!!')
        else:
            print(f'Скорость: {self.speed} км/ч')


class WorkCar(Car):
    speed_limit = 40
    def __init__(self, speed, color, name, is_police=bool):
        super().__init__(speed, color, name, is_police=bool)

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Скорость: {self.speed} км/ч\n'
                  f'Превышение скорости на {self.speed - self.speed_limit} км/ч !!!')
        else:
            print(f'Скорость: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=bool):
        super().__init__(speed, color, name, is_police=bool)

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч\n')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')



# print('\n|Класс Car|')
# car = Car(100, 'black', 'BMW', False)
# car.go()
# car.turn('лево')
# car.show_speed()
# car = Car(0,'black', 'BMW', False)
# car.stop()
# car.police_activity()

print('\n|Класс WorkCar|')
wcar = WorkCar(40, 'жёлтый', 'CAT')
wcar.police_activity()
wcar.go()
wcar.show_speed()
wcar.turn('право')
wcar = WorkCar(0, 'жёлтый', 'CAT')
wcar.show_speed()
wcar.stop()

print('\n|Класс TownCar|')
tcar = TownCar(70, 'белая', 'Audi')
tcar.police_activity()
tcar.go()
tcar.show_speed()
tcar.turn('назад')
tcar = TownCar(50, 'белая', 'Audi')
tcar.show_speed()
tcar.stop()

print('\n|Класс SportCar|')
scar = SportCar(200, 'чёрный', 'Lamborgini', False)
scar.police_activity()
scar.go()
scar.turn('лево')
scar.show_speed()

print('\n|Класс PoliceCar|')
pcar = PoliceCar(0, 'синяя', 'Ford', True)
pcar.show_speed()
pcar.police_activity()
pcar = PoliceCar(160, 'синяя', 'Ford', True)
pcar.go()
pcar.show_speed()
