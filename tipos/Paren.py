from Tipo import Tipo

class Paren(Tipo):
  def __init__(self, t):
    self.t = t

  def __str__(self):
    return "(%s)" % self.t
