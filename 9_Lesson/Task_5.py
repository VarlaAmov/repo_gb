class Stationery:
    title = 'отрисовки'

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    title = 'отрисовки'

    def draw(self):
        print(f'Запуск ручки')


class Pencil(Stationery):
    title = 'отрисовки'

    def draw(self):
        print(f'Запуск карандаша')


class Handle(Stationery):
    title = 'отрисовки'

    def draw(self):
        print(f'Запуск маркера')



st = Stationery()
st.draw()

pen = Pen()
pen.draw()

pensil = Pencil()
pensil.draw()

hand = Handle()
hand.draw()