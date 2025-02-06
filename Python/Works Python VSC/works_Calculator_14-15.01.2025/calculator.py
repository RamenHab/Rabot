class Calculator:
    def __init__(self):
        pass 

    def calc_sum(self, a, b):
        return a + b

    def calc_multiply(self, a, b):
        return a * b

    def calc_subtract(self, a, b):
        return a - b

    def calc_divide(self, a, b):
        return a / b

calc = Calculator()
print(calc.calc_sum(6,3))
print(calc.calc_multiply(6,3))
print(calc.calc_subtract(6,3))
print(calc.calc_divide(6,3))
