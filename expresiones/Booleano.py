from Expresion import Expresion

class Booleano(Expresion):
  def __init__(self, value):
    self.value = value

  def __eq__(self, other):
    if (isinstance(other, Booleano)):
      return self.value == self.value
    else:
      return False

  def __ne__(self, other):
    return not (self == other)

  def __str__(self):
    return "bool(%s)" % self.value
