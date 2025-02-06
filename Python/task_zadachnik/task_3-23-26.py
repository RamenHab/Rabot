class Number:
    def __init__(self, number):
        self.number = str(number)

    def task23(self):
        #Перемещает последнюю цифру в начало.
        last_digit = self.number[-1]
        remaining_digits = self.number[:-1]
        return int(last_digit + remaining_digits)
        
    def task24(self):
        #Меняет местами первое и второе число.
        return int(self.number[1] + self.number[0] + self.number[2])

    def task25(self):
        #Меняет местами второе и третье число.
        return int(self.number[0] + self.number[2] + self.number[1])
    
    def task26(self):
        #Перетановка чисел.
        digits = list(self.number)
        permutations = []
        import itertools #Модуль для генерации всех возможных чисел.
        for p in itertools.permutations(digits):
             permutations.append(int("".join(p)))
        return permutations

manipulator = Number(456)
print(f"3.23 - Результат: {manipulator.task23()}")
print(f"3.24 - Результат: {manipulator.task24()}")
print(f"3.25 - Результат: {manipulator.task25()}")
print("3.26 - Результаты перестановок:", manipulator.task26())