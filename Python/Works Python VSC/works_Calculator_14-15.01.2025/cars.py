class Car:
    def __init__(self, color, type, year):
        self.color=color
        self.type=type
        self.year=year

    def starting_the_car (self):
        return "Автомобиль заведен"
    
    def turning_off_the_car (self):
        return "Автомобиль заглушен"
    
    def year_of_release (self):
        return f"Автомобиль {self.year} года выпуска"
    
    def type_car (self):
        return f"Марка автомобиля {self.type}"
    
    def color_car (self):
        return f"Автомобиль {self.color} цвета"
    
car = Car("Red","Lada","1981")
print(car.starting_the_car())
print(car.turning_off_the_car())
print(car.year_of_release())
print(car.type_car())
print(car.color_car())