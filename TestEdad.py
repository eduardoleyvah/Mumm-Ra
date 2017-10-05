import unittest

from Edad import Edad

class EdadTest(unittest.TestCase):

	def setUp(self):
		self.operaciones = Edad()

	def test_edad_menor_a_0_no_existes(self):
		self.operaciones.obtener_edad(-1)
		self.assertEquals(self.operaciones.obtener_resultado(),'No existes')	

	def test_edad_menor_a_13_eres_ninio(self):
		self.operaciones.obtener_edad(10)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres ninio')

	def test_edad_menor_a_18_eres_adolescente(self):
		self.operaciones.obtener_edad(15)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres adolescente')

	def test_edad_menor_a_65_eres_adulto(self):
		self.operaciones.obtener_edad(33)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres adulto')	

	def test_edad_menor_a_120_eres_adulto_mayor(self):
		self.operaciones.obtener_edad(105)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres adulto mayor')	

	def test_edad_mayor_a_120_eres_mummra(self):
		self.operaciones.obtener_edad(200)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres Mumm-Ra')

if __name__ == '__main__': #pragma: no cover
	unittest.main()