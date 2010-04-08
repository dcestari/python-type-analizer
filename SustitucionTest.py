from Sustitucion import Sustitucion

from tipos.Bool import Bool
from tipos.Int import Int
from tipos.Fun import Fun
from tipos.Paren import Paren
from tipos.Var import Var

import unittest

import sys

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
    self.assertEqual(str(s.find(Var('a'))), str(Fun(Var('x'), Var('y'))))

  def test_sustituir(self):
    s = Sustitucion()
    s.push(Var('a'), Fun(Var('b'), Int()))
    self.assertEqual(
      str(s.sustituir(Fun(Var('a'), Var('b')))),
      str(Fun(Fun(Var('b'), Int()), Var('b')))
    )

  def test_sustituir_vacio(self):
    s = Sustitucion()
    self.assertEqual(
      str(s.sustituir(Fun(Var('a'), Var('b')))),
      str(Fun(Var('a'), Var('b')))
    )

  def test_sustituir_tipo_base(self):
    s = Sustitucion()
    s.push(Var('a'), Fun(Var('b'), Int()))
    self.assertEqual(
      str(s.sustituir(Int())),
      str(Int())
    )
    self.assertEqual(
      str(s.sustituir(Bool())),
      str(Bool())
    )

  def test_sustituir_paren(self):
    s = Sustitucion()
    s.push(Var('a'), Fun(Var('b'), Int()))
    self.assertEqual(
      str(s.sustituir(Paren(Var('a')))),
      str(Paren(Fun(Var('b'), Int())))
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
    
    a = map(lambda e: (str(e[0]), str(e[1])), s.all())

    self.assertEqual(
      a,
      [
        (str(Var('a')), str(Fun(Bool(), Int()))),
        (str(Var('w')), str(Fun(Int(), Fun(Bool(), Bool())))),
        (str(Var('b')), str(Bool())),
        (str(Var('c')), str(Int())),
      ]
    )

suite = unittest.TestLoader().loadTestsFromTestCase(SustitucionTest)
unittest.TextTestRunner(verbosity=2).run(suite)
