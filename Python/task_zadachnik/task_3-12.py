class Building:
    def __init__(self):
      self.apartments = 20 // 5

    def info(self, apartment_number):
        floor = (apartment_number - 1) // self.apartments + 1
        apartment_number_on_floor = (apartment_number - 1) % self.apartments + 1
        return floor, apartment_number_on_floor

five_story = Building()
floor, apartment_on_floor = five_story.info(13)
print(f"Этаж: {floor}, Квартира по счету: {apartment_on_floor}")  