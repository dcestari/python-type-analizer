from tipos.Bool import Bool
from tipos.Fun import Fun
from tipos.Int import Int
from tipos.Paren import Paren
from tipos.Var import Var

from utils.Sustitucion import Sustitucion
from utils.UnifyException import UnifyException

import unittest

class TipoTest(unittest.TestCase):
  def setUp(self):
    pass

  def test_unify_var(self):
    a = Var('a')
    b = Fun(Int(), Bool())

    s = Sustitucion()
    s.push(Var('a'), Fun(Int(), Bool()))
    
    self.assertEqual(a.unify(b), s)

  def test_unify_fun_fun(self):
    a = Fun(Fun(Var('a'), Int()), Var('a'))
    b = Fun(Var('b'), Fun(Var('c'), Int()))

    s = Sustitucion()
    s.push(Var('a'), Fun(Var('c'), Int()))
    s.push(Var('b'), Fun(Fun(Var('c'), Int()), Int()))

    self.assertEqual(a.unify(b), s)

  def test_unify_fun_var(self):
    a = Fun(Fun(Var('a'), Int()), Var('a'))
    b = Var('b')

    s = Sustitucion()
    s.push(Var('b'), Fun(Fun(Var('a'), Int()), Var('a')))

    self.assertEqual(a.unify(b), s)

  def test_unify_bool_int(self):
    a = Bool()
    b = Int()

    self.assertRaises(UnifyException, a.unify, b)

  def test_unify_paren(self):
    a = Fun(Paren(Paren(Fun(Var('a'), Int()))), Var('a'))
    b = Fun(Paren(Var('b')), Paren(Fun(Var('c'), Paren(Int()))))

    s = Sustitucion()
    s.push(Var('b'), Fun(Fun(Var('c'), Int()), Int()))
    s.push(Var('a'), Fun(Var('c'), Int()))

    self.assertEqual(a.unify(b), s)

  def test_unify_simple(self):
    a = Fun(Var('a'), Var('b'))
    b = Fun(Bool(), Int())

    s = Sustitucion()
    s.push(Var('a'), Bool())
    s.push(Var('b'), Int())

    self.assertEqual(a.unify(b), s)

suite = unittest.TestLoader().loadTestsFromTestCase(TipoTest)
unittest.TextTestRunner(verbosity=2).run(suite)
