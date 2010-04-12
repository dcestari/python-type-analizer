from utils.Ambiente import Ambiente
from utils.AssignException import AssignException
from utils.Sustitucion import Sustitucion
from utils.UnifyException import UnifyException

from expresiones.Aplicacion import Aplicacion
from expresiones.Booleano import Booleano
from expresiones.Conjuncion import Conjuncion
from expresiones.Entero import Entero
from expresiones.Lambda import Lambda
from expresiones.MenorQue import MenorQue
from expresiones.Suma import Suma
from expresiones.Variable import Variable

from tipos.Bool import Bool
from tipos.Fun import Fun
from tipos.Int import Int
from tipos.Var import Var

import unittest

class AmbienteTest(unittest.TestCase):
  def setUp(self):
    pass

  def test_find_empty(self):
    a = Ambiente()
    self.assertEqual(a.find(Variable('x')), None)

  def test_extend_find_existing(self):
    a = Ambiente()
    a.extend(Variable('x'), Int())
    self.assertEqual(a.find(Variable('x')), Int())

  def test_extend_find_non_existing(self):
    a = Ambiente()
    a.extend(Variable('x'), Int())
    self.assertEqual(a.find(Variable('y')), None)

  def test_assign_entero_int(self):
    a = Ambiente()
    self.assertEqual(a.assign(Entero(12), Int()), Sustitucion())

  def test_assign_entero_fun(self):
    a = Ambiente()
    self.assertRaises(UnifyException, a.assign, Entero(12), Fun(Int(), Int()))

  def test_assign_booleano_bool(self):
    a = Ambiente()
    self.assertEqual(a.assign(Booleano(True), Bool()), Sustitucion())

  def test_assign_booleano_fun(self):
    a = Ambiente()
    self.assertRaises(UnifyException, a.assign, Booleano(True), Fun(Int(), Int()))

  def test_assign_variable_int(self):
    a = Ambiente()
    a.extend(Variable('x'), Var('a'))

    s = Sustitucion()
    s.push(Var('a'), Int())

    self.assertEqual(a.assign(Variable('x'), Int()), s)

  def test_assign_non_existent_variable_int(self):
    a = Ambiente()
    self.assertRaises(AssignException, a.assign, Variable('x'), Int())

  def test_assign_suma_int(self):
    a = Ambiente()
    self.assertEqual(a.assign(Suma(Entero(12), Entero(14)), Int()), Sustitucion())

  def test_assign_suma_bool(self):
    a = Ambiente()
    self.assertRaises(UnifyException, a.assign, Suma(Entero(10), Entero(40)), Bool())

  def test_assign_menorque_bool(self):
    a = Ambiente()
    self.assertEqual(a.assign(MenorQue(Entero(12), Entero(14)), Bool()), Sustitucion())

  def test_assign_menorque_int(self):
    a = Ambiente()
    self.assertRaises(UnifyException, a.assign, MenorQue(Entero(10), Entero(40)), Int())

  def test_assign_conjuncion_bool(self):
    a = Ambiente()
    self.assertEqual(a.assign(Conjuncion(Booleano(True), Booleano(False)), Bool()), Sustitucion())

  def test_assign_conjuncion_int(self):
    a = Ambiente()
    self.assertRaises(UnifyException, a.assign, Conjuncion(Booleano(True), Booleano(False)), Int())

  def test_assign_lambda_fun(self):
    a = Ambiente()
    
    s = Sustitucion()
    s.push(Var('a'), Bool())
    s.push(Var('b'), Int())

    self.assertEqual(a.assign(Lambda(Variable('x'), Entero(12)), Fun(Bool(), Int())), s)

  def test_assign_aplicar_int(self):
    a = Ambiente()
    
    x = Aplicacion(Lambda(Variable('x'), Suma(Variable('x'), Entero(1))), Entero(12))
    y = Int()
    
    s = Sustitucion()
    s.push(Var('a'), Int())
    s.push(Var('b'), Int())

    self.assertEqual(a.assign(x, y), s)


suite = unittest.TestLoader().loadTestsFromTestCase(AmbienteTest)
unittest.TextTestRunner(verbosity=2).run(suite)
