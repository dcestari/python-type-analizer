from Tipo import Tipo
from utils.Sustitucion import Sustitucion

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

  def unify(self, t):
    if (isinstance(t, Fun)):
      s_domain = self.domain.unify(t.domain)
      s_range = self.range.unify(t.range).compose(s_domain)

      try:
        s_self = self.domain.unify(self.range)
      except:
        s_self = Sustitucion()

      try:
        s_t = t.domain.unify(t.range)
      except:
        s_t = Sustitucion()

      return s_range.compose(s_domain.compose(s_t.compose(s_self.compose(s_range))))
    else:
      return t.unify(self)
