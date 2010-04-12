from Booleano import Booleano

class Conjuncion(Booleano):
  def __init__(self, lvalue, rvalue):
    self.lvalue = lvalue
    self.rvalue = rvalue

  def __eq__(self, other):
    if (isinstance(other, Conjuncion)):
      return self.lvalue == other.lvalue and self.rvalue == other.rvalue
    else:
      return False

  def __ne__(self, other):
    return not (self == other)

  def __str__(self):
    return "%s /\ %s" % (self.lvalue, self.rvalue)
