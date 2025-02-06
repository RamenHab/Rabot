class Building:
    def __init__(self):
      self.floors = 9
      self.apartments_per_floor = 6
      self.entrances = 4

    def info(self, apartment_number):
        apartments_entrance = self.floors * self.apartments_per_floor
        entrance = (apartment_number - 1) // apartments_entrance + 1
        apartments_in_current_entrance = apartment_number - (entrance - 1) * apartments_entrance
        floor = (apartments_in_current_entrance - 1) // self.apartments_per_floor + 1
        apartment_number_on_floor = (apartments_in_current_entrance - 1) % self.apartments_per_floor + 1
        return entrance, floor, apartment_number_on_floor

nine_story = Building()
entrance, floor, apartment_on_floor = nine_story.info(148)
print(f"Подъезд: {entrance}, Этаж: {floor}, Квартира по счету: {apartment_on_floor}")