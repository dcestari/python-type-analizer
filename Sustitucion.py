from tipos.Bool import Bool
from tipos.Int import Int
from tipos.Fun import Fun
from tipos.Paren import Paren
from tipos.Var import Var

import sys

class Sustitucion:
  def __init__(self, pairs = None):
    "pairs = [(a, T1), (b, T2), ... , (z, Tn)]"

    if (pairs == None):
      self.pairs = []
    else:
      self.pairs = pairs

  def push(self, a, t):
    self.pairs.append((a, t))

  def pop(self):
    return self.pairs.pop()

  def contains(self, v):
    s = self.find(v)
    return s != None

  def find(self, v):
    s = filter(lambda e: (e[0].symbol == v.symbol), self.pairs)
    if (len(s) > 0):
      return s.pop()[1]
    else:
      return None

  def size(self):
    return len(self.pairs)

  def sustituir(self, t):
    if (isinstance(t, Fun)):
      t.domain = self.sustituir(t.domain)
      t.range = self.sustituir(t.range)
      return t
    elif(isinstance(t, Var)):
      e = self.find(t)
      if (e != None): return e
    elif(isinstance(t, Paren)):
      t.t = self.sustituir(t.t)

    return t

  def all(self):
    return self.pairs

  def compose(self, s):
    new_pairs = map(
      lambda e: (e[0], s.sustituir(e[1])),
      self.pairs
    )
    new_pairs.extend(filter(
      lambda e: (self.find(e[0]) == None),
      s.pairs
    ))

    return Sustitucion(new_pairs)
