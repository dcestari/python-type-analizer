from Expresion import Expresion

class Aplicacion(Expresion):
  def __init__(self, f, x):
    self.f = f
    self.x = x

  def __eq__(self, other):
    if (isinstance(other, Aplicacion)):
      return self.f == other.f and self.x == other.x
    else:
      return False

  def __ne__(self, other):
    return not (self == other)

  def __str__(self):
    return "%s %s" % (self.f, self.x)
