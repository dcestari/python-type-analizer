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
    if (t.tipo == 'Fun'):
      t.domain = self.sustituir(t.domain)
      t.range = self.sustituir(t.range)
      return t
    elif(t.tipo == 'Var'):
      e = self.find(t)
      if (e != None): return e
    elif(t.tipo == 'Paren'):
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

  def __eq__(self, other):
    if (isinstance(other, Sustitucion)):
      return sorted(self.pairs, key=lambda e: e[0].symbol) == sorted(other.pairs, key=lambda e: e[0].symbol)
    else:
      return False

  def __ne__(self, other):
    return not (self == other)

  def __str__(self):
    strs = map(lambda e: (str(e[0]), str(e[1])), sorted(self.pairs, key=lambda e: e[0].symbol))
    return str(strs)
