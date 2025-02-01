class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.__year = year
        self.color = color

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value > 1900:
            self.__year = value

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Цвет: {self.color}")

class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity
    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Цвет: {self.color}")
        print(f"Заряд: {self.battery_capacity}")


my_car_1 = Car("Toyota", "Camry", 2020, "red")
my_car_2 = ElectricCar("Tesla", "Model S", 2023, "blue", 100)


my_car_1.display_info()
my_car_2.display_info()











