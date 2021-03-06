# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    __color = 'green'
    def __init__(self, running=False):
        self.running = running
    def TrafficLight_ch(self):
        if self.running == True:
            self.color = 'red'
            print(f'Светофор горит {self.color}!')
            time.sleep(7)
            self.color = 'yellow'
            print(f'Светофор горит {self.color}!')
            time.sleep(2)
            #self.color = 'green'


a = TrafficLight(running=True)
a.TrafficLight_ch()
print(f'Светофор горит {a._TrafficLight__color}!')