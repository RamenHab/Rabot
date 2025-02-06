class Distance:
    def __init__(self, santi):
        self.santi = santi

    def meter(self):
        return int(self.santi // 100)

distance = Distance(2000)
print(f"Полных метров: {distance.meter()}")