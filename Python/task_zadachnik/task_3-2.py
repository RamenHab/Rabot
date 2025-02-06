class Weight:
    def __init__(self, kilograms):
      self.kilograms = kilograms

    def centners(self):
        return int(self.kilograms // 100)

weight = Weight(12345)
print(f"Полных центнеров: {weight.centners()}")