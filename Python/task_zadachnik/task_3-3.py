class Time:
    def __init__(self, days):
        self.days = days

    def weeks(self):
        return int(self.days // 7)

time = Time(333)
print(f"Полных недель: {time.weeks()}")