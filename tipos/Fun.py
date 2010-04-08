from Tipo import Tipo

class Fun(Tipo):
  "T1 --> T2"
  def __init__(self, domain, range):
    self.domain = domain
    self.range = range

  def __str__(self):
    return  "%s --> %s" % (self.domain, self.range)
