class Dog:
    def __init__(self, height, weight, color, wool):
        self.height=height
        self.weight=weight
        self.color=color
        self.wool=wool

    def dogone (self):
        return f"Моя собака ростом {self.height}, вес у нее {self.weight}, она {self.color}, и {self.wool}"
    
class Sheepdog(Dog):
    def __init__(self, height, weight, color, wool, age):
        super().__init__(height, weight, color, wool)
        self.age = age
    
    def dogtwo (self):
        return f"Моя собака такая же ростом {self.height} и вес у нее {self.weight}, но цвет у нее {self.color} и не {self.wool}. И возвраст собаки {self.age}"
    

animal=Dog("45","15","Red","fluffy")
print(animal.dogone())

sheepdog = Sheepdog("15","10","Blue","NOfluffy","5")
print(sheepdog.dogone())
print(sheepdog.dogtwo())