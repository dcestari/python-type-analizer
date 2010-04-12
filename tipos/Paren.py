from Tipo import Tipo

class Paren(Tipo):
  def __init__(self, t):
    self.tipo = "Paren"
    self.t = t

  def __str__(self):
    return "(%s)" % self.t

  def __eq__(self, other):
    if (isinstance(other, Paren)):
      return self.t == other.t
    else:
      return False

  def __ne__(self, other):
    return not (self == other)
