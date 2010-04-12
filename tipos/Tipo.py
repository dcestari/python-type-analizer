from utils.UnifyException import UnifyException

class Tipo:
  def __str__(self):
    return "T"

  def unify(self, t):
    if(self == t):
      return Sustitucion()
    elif(t.tipo == "Var"):
      return t.unify(self)
    else:
      raise UnifyException(self, t)

