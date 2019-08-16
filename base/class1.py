# -*- coding:utf-8 -*-
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """电动汽车的独特之处 初始化父类的属性，再初始化电动汽车特有的属性 """
        super().__init__(make, model, year)
        self.battery_size = 70
