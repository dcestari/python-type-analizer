from Expresion import Expresion

class Entero(Expresion):
  def __init__(self, value):
    self.value = value

  def __eq__(self, other):
    if (isinstance(other, Entero)):
      return self.value == other.value
    else:
      return False

  def __ne__(self, other):
    return not (self == other)

  def __str__(self):
    return "int(%s)" % self.value
