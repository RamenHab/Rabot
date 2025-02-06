import math

class task:
    def print_task(self, number, precision):
       print(f"{number:.{precision}f}")

printer = task()
printer.print_task(math.e, 1)