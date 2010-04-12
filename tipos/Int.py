from Tipo import Tipo

class Int(Tipo):
  def __init__(self):
    self.tipo = "Int"
  
  def __str__(self):
    return "int"

  def __eq__(self, other):
    return isinstance(other, Int)

  def __ne__(self, other):
    return not (self == other)
