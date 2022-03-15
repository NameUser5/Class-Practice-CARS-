class Prices():
  #How can I set a default currency?
  def __init__(self, base_price, mid_price = 0, deluxe_price = 0):
    self.base_price = base_price
    self.mid_price = mid_price
    self.deluxe_price = deluxe_price