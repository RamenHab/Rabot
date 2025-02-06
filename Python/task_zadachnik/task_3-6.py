class Train:
    def __init__(self, number):
        self.number = number

    def cupe_number(self):
        return (self.number - 1) // 4 + 1

train = Train(23)
print(f"Номер купе: {train.cupe_number()}")
