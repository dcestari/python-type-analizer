from Tipo import Tipo

class Bool(Tipo):
  def __str__(self):
    return "bool"

  def __eq__(self, other):
    return isinstance(other, Bool)

  def __ne__(self, other):
    return not (self == other)
