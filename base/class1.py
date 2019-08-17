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


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """ 初始化父类的属性，再初始化电动汽车特有的属性 """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
