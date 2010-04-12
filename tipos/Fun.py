from Tipo import Tipo

class Fun(Tipo):
  "T1 --> T2"
  def __init__(self, domain, range):
    self.tipo = "Fun"
    self.domain = domain
    self.range = range

  def __str__(self):
    return  "%s --> %s" % (self.domain, self.range)

  def __eq__(self, other):
    if (isinstance(other, Fun)):
      return self.domain == other.domain and self.range == other.range
    else:
      return False

  def __ne__(self, other):
    return not (self == other)

