from expresiones.Aplicacion import Aplicacion
from expresiones.Booleano import Booleano
from expresiones.Conjuncion import Conjuncion
from expresiones.Entero import Entero
from expresiones.Lambda import Lambda
from expresiones.MenorQue import MenorQue
from expresiones.Variable import Variable
from expresiones.Suma import Suma

from tipos.Bool import Bool
from tipos.Fun import Fun
from tipos.Int import Int
from tipos.Var import Var

from utils.AssignException import AssignException
from utils.Sustitucion import Sustitucion

class Ambiente:
  def __init__(self):
    self.pairs = []
  
  def extend(self, x, t):
    self.pairs.append((x, t))

  def find(self, v):
    s = filter(lambda e: (e[0].name == v.name), self.pairs)
    if (len(s) > 0):
      return s.pop()[1]
    else:
      return None

  def assign(self, e, t):
    if (isinstance(e, Variable)):
      amb_x = self.find(e)

      if (amb_x == None):
        raise AssignException(str(e), str(t))
      else:
        return t.unify(amb_x)
    elif (isinstance(e, Suma)):
      s1 = self.assign(e.lvalue, Int())
      s2 = s1.compose(self.assign(e.rvalue, Int()))
      return s2.compose(t.unify(Int()))
    elif (isinstance(e, MenorQue)):
      s1 = self.assign(e.lvalue, Int())
      s2 = s1.compose(self.assign(e.rvalue, Int()))
      return s2.compose(t.unify(Bool()))
    elif (isinstance(e, Conjuncion)):
      s1 = self.assign(e.lvalue, Bool())
      s2 = s1.compose(self.assign(e.rvalue, Bool()))
      return s2.compose(t.unify(Bool()))
    elif (isinstance(e, Lambda)):
      a = Var('a')
      b = Var('b')
      self.extend(e.x, a)
      s1 = self.assign(e.e, b)
      return s1.compose(t.unify(s1.sustituir(Fun(a, b))))
    elif (isinstance(e, Aplicacion)):
      a = Var('a')
      s1 = self.assign(e.x, a)
      return s1.compose(self.assign(e.f, Fun(s1.sustituir(a), t)))
    elif (isinstance(e, Entero)):
      return t.unify(Int())
    elif (isinstance(e, Booleano)):
      return t.unify(Bool())
    else:
      raise AssignException(str(e), str(t))
