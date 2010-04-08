from Tipo import Tipo

class Var(Tipo):
  def __init__(self, symbol):
    self.symbol = symbol

  def __str__(self):
    return "%s" % self.symbol
