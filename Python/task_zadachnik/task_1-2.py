import math

class task:
    def print_task(self, numbers):
        print(*numbers, sep="  ")

printer = task()
printer.print_task([23, 345, 654])