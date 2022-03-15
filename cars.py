class Cars():
  axles = 2

  def __init__(self, make, model, year = 0, color = "", seats = ""):
    self.make = make
    self.model = model
    self.year = year
    self.color = color
    self.seats = seats

  def car_sounds(self):
    print(f'{self.model} goes "Vrooooooom!"')

  def alt_year(self):
    print(self.year + 10) # different result from not putting the print here
