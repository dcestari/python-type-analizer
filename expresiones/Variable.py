from Expresion import Expresion

class Variable(Expresion):
  def __init__(self, name):
    self.name = name

  def __eq__(self, other):
    if (isinstance(other, Variable)):
      return self.name == other.name
    else:
      return False

  def __ne__(self, other):
    return not (self == other)

  def __str__(self):
    return "var(%s)" % self.name