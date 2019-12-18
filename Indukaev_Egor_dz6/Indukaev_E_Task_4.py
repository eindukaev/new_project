# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class Car:
    def __init__(self, speed=None, color='', name='', **kwargs):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = None
        self.is_police = False


    def go(self):
        print(f'Машина марки -- {self.name} поехала!')


    def stop(self):
        print(f'Машина марки -- {self.name} остановилась!')


    def turn(self):
        if self.direction == 'лево':
            print(f'Машина марки -- {self.name} повернула на{self.direction}!')
        elif self.direction == 'право':
            print(f'Машина марки -- {self.name} повернула на{self.direction}!')


    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed} км.ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысил скоростной режим 60 км.ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превысил скоростной режим 40 км.ч')


class PoliceCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_police = True


car_1 = PoliceCar(speed=210, color='red', name='Lexus', is_police=True)
car_2 = TownCar(speed=61, color='white', name='Газель')
car_3 = WorkCar(speed=210, color='black', name='Mercedes')
#car_1 = ()
print(car_1.name, car_1.color, car_1.speed, car_1.is_police)
car_1.show_speed()
car_1.go()
car_1.direction = 'лево'
car_1.turn()
print(car_2.name, car_2.color, car_2.speed)
car_2.direction = 'право'
car_2.turn()
car_2.show_speed()
car_2.stop()
print(car_3.name, car_3.color, car_3.speed, car_3.is_police)
car_3.direction = 'лево'
car_3.turn()
car_3.show_speed()


