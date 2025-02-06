class pramo:
  def __init__(self, width, height, side):
    self.width = width
    self.height = height
    self.side = side

  def res(self):
        return int(self.width // self.side) * int(self.height // self.side)
  

rez = pramo(543, 130, 130)
print(f"Можно отрезать {rez.res()} квадратов")