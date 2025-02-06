class Calculator:
    def __init__(self, number):
        self.number = number

    def calculate_sum(self):
        sum_digits = sum(int(digit) for digit in str(self.number))
        return sum_digits

num1 = Calculator(1234)
print(f"Сумма 4-значного числа {num1.number}: {num1.calculate_sum()}") 
num2 = Calculator(56789)
print(f"Сумма 5-значного числа {num2.number}: {num2.calculate_sum()}") 