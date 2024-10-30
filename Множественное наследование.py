# Класс Horse, описывающий лошадь
class Horse:
    def __init__(self):
        self.x_distance = 0         # Пройденный путь по горизонтали
        self.sound = 'Frrr'         # Звук, который издаёт лошадь

    # Метод для увеличения пройденного пути
    def run(self, dx):
        self.x_distance += dx

# Класс Eagle, описывающий орла
class Eagle:
    def __init__(self):
        self.y_distance = 0           # Высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издаёт орёл

    # Метод для увеличения высоты полёта
    def fly(self, dy):
        self.y_distance += dy

# Класс Pegasus, наследник от Horse и Eagle
class Pegasus(Horse, Eagle):
    def __init__(self):
        # Инициализируем классы родителей
        Horse.__init__(self)
        Eagle.__init__(self)

    # Метод для перемещения пегаса, изменяющий x и y
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    # Метод возвращает текущую позицию (x, y)
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    # Метод выводит звук, который издаёт Pegasus
    def voice(self):
        print(self.sound)

# Проверка работы программы
p1 = Pegasus()

# Проверка позиции
print(p1.get_pos())         # (0, 0)

# Перемещение и проверка позиции
p1.move(10, 15)
print(p1.get_pos())         # (10, 15)

# Ещё одно перемещение и проверка позиции
p1.move(-5, 20)
print(p1.get_pos())         # (5, 35)

# Проверка голоса пегаса
p1.voice()                  # I train, eat, sleep, and repeat
