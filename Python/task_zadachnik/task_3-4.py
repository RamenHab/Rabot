class Apple:
    def __init__(self, student, apple):
        self.student = student
        self.apple = apple

    def apples(self):
      applesss = self.apple // self.student
      appless = self.apple % self.student
      return applesss, appless

apples = Apple(15, 100)
applesss, appless = apples.apples()
print(f"Яблок на школьника: {applesss}, Осталось в корзинке: {appless}")