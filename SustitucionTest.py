from utils.Sustitucion import Sustitucion

from tipos.Bool import Bool
from tipos.Int import Int
from tipos.Fun import Fun
from tipos.Paren import Paren
from tipos.Var import Var

import unittest

class SustitucionTest(unittest.TestCase):
  def setUp(self):
    pass

  def test_push(self):
    s = Sustitucion()
    self.assertEqual(s.size(), 0)
    s.push(Var('a'), Int())
    self.assertEqual(s.size(), 1)

  def test_pop(self):
    s = Sustitucion()
    s.push(1, 2)
    self.assertEqual(s.pop(), (1, 2))

  def test_size(self):
    s = Sustitucion()
    self.assertEqual(s.size(), 0)
    s.push(1, 2)
    self.assertEqual(s.size(), 1)
    s.pop()
    self.assertEqual(s.size(), 0)

  def test_contains(self):
    s = Sustitucion()
    self.assertFalse(s.contains(Var('x')))
    s.push(Var('a'), 1)
    self.assertTrue(s.contains(Var('a')))

  def test_find(self):
    s = Sustitucion()
    s.push(Var('a'), Fun(Var('x'), Var('y')))
    self.assertEqual(s.find(Var('a')), Fun(Var('x'), Var('y')))

  def test_sustituir(self):
    s = Sustitucion()
    s.push(Var('a'), Fun(Var('b'), Int()))
    self.assertEqual(
      s.sustituir(Fun(Var('a'), Var('b'))),
      Fun(Fun(Var('b'), Int()), Var('b'))
    )

  def test_sustituir_vacio(self):
    s = Sustitucion()
    self.assertEqual(
      s.sustituir(Fun(Var('a'), Var('b'))),
      Fun(Var('a'), Var('b'))
    )

  def test_sustituir_tipo_base(self):
    s = Sustitucion()
    s.push(Var('a'), Fun(Var('b'), Int()))
    self.assertEqual(
      s.sustituir(Int()),
      Int()
    )
    self.assertEqual(
      s.sustituir(Bool()),
      Bool()
    )

  def test_sustituir_paren(self):
    s = Sustitucion()
    s.push(Var('a'), Fun(Var('b'), Int()))
    self.assertEqual(
      s.sustituir(Paren(Var('a'))),
      Paren(Fun(Var('b'), Int()))
    )

  def test_compose(self):
    s1 = Sustitucion()
    s1.push(Var('a'), Fun(Var('b'), Int()))
    s1.push(Var('w'), Fun(Var('c'), Fun(Var('b'), Bool())))
    s2 = Sustitucion()
    s2.push(Var('b'), Bool())
    s2.push(Var('c'), Int())
    s2.push(Var('a'), Bool())
    s2.push(Var('w'), Int())
    s = s1.compose(s2)

    self.assertEqual(
      s.all(),
      [
        (Var('a'), Fun(Bool(), Int())),
        (Var('w'), Fun(Int(), Fun(Bool(), Bool()))),
        (Var('b'), Bool()),
        (Var('c'), Int()),
      ]
    )

  def test_compose_simple(self):
    s1 = Sustitucion()
    s1.push(Var('a'), Fun(Var('c'), Int()))
    s2 = Sustitucion()
    s2.push(Var('b'), Fun(Var('a'), Int()))
    s = Sustitucion()
    s.push(Var('a'), Fun(Var('c'), Int()))
    s.push(Var('b'), Fun(Var('a'), Int()))

    self.assertEqual(s1.compose(s2), s)

suite = unittest.TestLoader().loadTestsFromTestCase(SustitucionTest)
unittest.TextTestRunner(verbosity=2).run(suite)
