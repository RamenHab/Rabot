import math

class task:
    def print_task(self):
         try:
            num = input("Введите число: ")
            print("Вы ввели число:", num)
         except ValueError:
            print("Ошибка: Введено некорректное значение")

printer = task()
printer.print_task()