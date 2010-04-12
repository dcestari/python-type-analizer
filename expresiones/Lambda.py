from Expresion import Expresion

class Lambda(Expresion):
  def __init__(self, x, e):
    self.x = x
    self.e = e

  def __eq__(self, other):
    if (isinstance(other, Lambda)):
      return self.x == other.x and self.e == other.e
    else:
      return False

  def __ne__(self, other):
    return not (self == other)

  def __str__(self):
    return "lambda %s.%s" % (self.x, self.e)
