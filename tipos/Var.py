from Tipo import Tipo

class Var(Tipo):
  def __init__(self, symbol):
    self.symbol = symbol

  def __str__(self):
    return "%s" % self.symbol

  def __eq__(self, other):
    if (isinstance(other, Var)):
      return self.symbol == other.symbol
    else:
      return False

  def __ne__(self, other):
    return not (self == other)
