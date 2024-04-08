import unittest

from suma import suma.py
class testsuma(unittest.TestCase):
    def test_suma(self):
      resultado = suma(2, 3)
      self.assertEqual(resultado, 5)
    
unittest.main()